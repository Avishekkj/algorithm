#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    diff = []
    arr.sort()
    for i in range(0,n):
        a = abs(arr[i] - arr[i - 1])
        diff.append(a)
    print("Smallest element is:", min(diff), diff)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))


    result = minimumAbsoluteDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()

#1 -3 71 68 17