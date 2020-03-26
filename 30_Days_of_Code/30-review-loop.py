#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        word = input();
        for j in range(0,len(word),2):
            print(word[j], end='')
        print(" ", end='')
        for j in range(1,len(word),2):
            print(word[j], end='')
        print ("")