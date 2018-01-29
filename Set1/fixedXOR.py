#! python3
# fixedXOR.py - Takes 2 equal length inputs and returns their XOR combination

import logging

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')


def fixedXOR(str1, str2):
    in1 = int(str1, 16)
    in2 = int(str2, 16)
    logging.debug(type(in1))
    logging.debug(type(in2))
    bin_out = hex(in1 ^ in2)[2:]
    logging.debug(bin_out)
    return bin_out


test1 = '1c0111001f010100061a024b53535009181c'
test2 = '686974207468652062756c6c277320657965'
fixedXOR(test1, test2)
