#! python3
# hex2base64.py - Converts a hex value to base64

import binascii
import logging

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')


# If program is correct string_test should be converted to string_result
string_test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
string_result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

hex_string = string_test

hex_binary = binascii.unhexlify(hex_string)
logging.debug(hex_binary)
base64_result = binascii.b2a_base64(hex_binary, newline=False).decode("utf-8")

print(base64_result)
logging.debug(base64_result == string_result)
