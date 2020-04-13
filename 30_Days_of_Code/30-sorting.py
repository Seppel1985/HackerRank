#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfTotalSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    
    for j in range(n-1):
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
            numberOfTotalSwaps += 1
            
    if (numberOfSwaps == 0):
        break

print ("Array is sorted in " + str(numberOfTotalSwaps) +" swaps.")
print ("First Element: "+str(a[0]))
print ("Last Element: "+str(a[n-1]))
