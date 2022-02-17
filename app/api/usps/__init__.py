from config import LOGGER
import sys
import requests

class USPS:
    BASE_URL = 'https://tools.usps.com'
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    def __init__(self, user_agent=None):
        self.headers = {
            'User-Agent': user_agent if user_agent else USPS.DEFAULT_USER_AGENT,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
            'Origin': USPS.BASE_URL,
            'Connection': 'keep-alive',
            'Referer': f'{USPS.BASE_URL}/zip-code-lookup.htm?byaddress',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

    def search(self, company_name, address, city, state, zip_code):
        result = False
        try:
            cookies = {
                'TLTSID': '5c00c9943815161e9a0800e0ed96ae55',
                'NSC_uppmt-usvf-ofx': 'ffffffff3b22378d45525d5f4f58455e445a4a4212d3',
                '_gcl_au': '1.1.366595644.1645085608',
                'mab_usps': '11',
                '_ga_3NXP3C8S9V': 'GS1.1.1645125024.2.1.1645125566.0',
                '_ga': 'GA1.2.135497153.1645085609',
                '_gid': 'GA1.2.69167682.1645085609',
                '_rdt_uuid': '1645085609518.0d33f9d1-6c3c-48e2-9a96-b0e78f7e23f7',
                '_scid': '8cdd7cc5-9d42-4649-bb2f-00a4642b999a',
                '_pin_unauth': 'dWlkPU5UZzBOMkU1TkRZdE5XUTVZeTAwWlRnMExXRm1ORFl0WVRRMFpHRTJORFZrWlRGaA',
                '_fbp': 'fb.1.1645085611223.676180434',
                'mdLogger': 'false',
                'kampyleUserSession': '1645125024903',
                'kampyleSessionPageCounter': '1',
                'kampyleUserSessionsCount': '3',
                '_sctr': '1|1645048800000',
                '_uetsid': '7d7811808fc911ec9941ab42bf83dd93',
                '_uetvid': '7d7821208fc911ec808c7d01b301554b',
            }
            if company_name and address and  city and  state and  zip_code:
                data = {
                    'companyName': str(company_name),
                    'address1': str(address),
                    'address2': '',
                    'city': str(city),
                    'state': str(state),
                    'urbanCode': '',
                    'zip': str(zip_code)
                }
                r = requests.post(f'{USPS.BASE_URL}/tools/app/ziplookup/zipByAddress', headers=self.headers, data=data)
                if r.status_code == 200:
                    json_data = r.json()
                    result = True if json_data.get('resultStatus', '').strip().upper() == 'SUCCESS' else False
            else:
                LOGGER.error(f"[{self.__class__.__name__}] [SEARCH] Not all parameters are filled in")
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            LOGGER.error(f"[{self.__class__.__name__}] [SEARCH] E:{exc} L:{exc_tb.tb_lineno}")
        finally:
            return result
