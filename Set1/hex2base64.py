#! python3
# hex2base64.py - Converts a hex value to base64

import logging
import base64

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')


# If program is correct string_test should be converted to string_result
string_test = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
string_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hex_string = string_test
logging.debug(len(hex_string))