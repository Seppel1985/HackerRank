#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    biggest_sum = -100
    for i in range(6-2):
        for j in range (6-2):
            sum_hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]  + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if (sum_hourglass > biggest_sum):
                biggest_sum = sum_hourglass
    print(biggest_sum)
