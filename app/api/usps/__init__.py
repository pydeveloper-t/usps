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
