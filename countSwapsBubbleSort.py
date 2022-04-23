#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    counts = 0
 
    for i in range(n-1):
 
        for j in range(0, n-i-1):

            if a[j] > a[j + 1] :
                a[j], a[j + 1] = a[j + 1], a[j]
                counts+=1
    
    print("Array is sorted in "+str(counts)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)