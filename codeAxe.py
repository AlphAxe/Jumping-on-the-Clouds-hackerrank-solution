#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    m=0
    while i<=len(c)-2:
        if c[i]==0:
            if i+2 == len(c):
                i+=1
                m+=1
            else:
                i+=2
                if c[i]==1:
                    i-=1
                    m+=1
                else:
                    m+=1
        else:
            i+=1
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
