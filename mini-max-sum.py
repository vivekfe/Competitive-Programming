#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    y = combinations(arr, 4)
    final_ls = []
    for item in y:
        final_ls.append(sum(list(item)))
    return min(final_ls), max(final_ls)
    #print('{0} {1}'.format(min(final_ls), max(final_ls)))


if __name__ == '__main__':
    arr = [1,3,5,7,9]
    assert miniMaxSum(arr)== (16,24)
