Address verification script
===========

The script performs address validation from the CSV input file on the https://tools.usps.com/zip-code-lookup.htm?byaddress page

 Requirements

- Python 3.9+

## App structure
-----------------
Project is structured in modules:
- app - Sources root
- --config      - Initialisation script
- --api--usps   - The class for working with https://tools.usps.com 	
- start_app.py  - Main script
- requirements.txt - A requirements file with a list of all of a project's dependencies


## Setup
- Install Python
- Create virtual environment (via pip or pipenv, etc )
- Activate virtual environment and install requirements
```
pip install -r requirements.txt
```

### Launch of the script
```
python app/start_app.py -i <Path to input CSV file>

```
The result will be placed in an output file located in the same directory as the input file, but with name 
```
<Input file name>out.csv

```
