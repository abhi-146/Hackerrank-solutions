#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    if sum(B)%2==1:
        print("NO")
    else:
        count =0
        l = len(B)
        for i in range(l):
            if B[i]%2!=0:
                B[i]+=1
                B[i+1]+=1
                count+=2
        print (count)


if __name__ == '__main__':
   

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    fairRations(B)

 
