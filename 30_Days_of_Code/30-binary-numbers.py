#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary_number = "{0:b}".format(n)
    cons_ones = 0
    max_int = 0
    for bit in binary_number:
        if (bit == '1'):
            cons_ones += 1
            max_int = cons_ones
        else:
            cons_ones = 0  
    print(max_int)   
