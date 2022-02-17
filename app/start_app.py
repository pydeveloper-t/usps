from config import LOGGER
from api.usps import USPS
import os
import csv
import argparse
import configparser

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Riskline Server')
    CONFIG = configparser.ConfigParser()
    argparser.add_argument('-i', '--inputfile', help='Path to source CSV file',required=True )
    input_file = argparser.parse_args().inputfile
    if not os.path.isfile(input_file):
        LOGGER.fatal(f'Not found source CSV file file: {input_file}')
        raise SystemExit
    usps = USPS()
    LOGGER.info(f"Input file {input_file}")
    output_file = os.path.join(os.path.dirname(input_file),os.path.splitext(os.path.basename(input_file))[0] + '.out.csv')
    LOGGER.info(f"Output file {output_file}")
    with open(output_file, 'w') as out_f:
        with open(input_file, 'r') as inp_f:
            csv_reader = csv.DictReader(inp_f)
            counter = 0
            for row in csv_reader:
                if not counter:
                    csv_writer = csv.DictWriter(out_f, fieldnames=list(row.keys()) + ['valid'])
                    csv_writer.writeheader()
                counter += 1
                LOGGER.info(f"[{counter}] {row}")
                valid = usps.search(
                    company_name=row['Company'],
                    address=row['Street'],
                    city=row['City'],
                    state=row['St'],
                    zip_code=row['ZIPCode']
                )
                LOGGER.info(f"\t Address is valid? {valid}")
                row.update({'valid': valid})
                csv_writer.writerow(row)
    LOGGER.info(f"Processed {counter} rows")



