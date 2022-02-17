import logging

MAX_HTTP_ATTEMPTS = 3
TAG = 'USPS'
LOGGER = logging.getLogger(f'{TAG}')
LOGGER.setLevel(logging.INFO)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
LOGGER.addHandler(c_handler)

