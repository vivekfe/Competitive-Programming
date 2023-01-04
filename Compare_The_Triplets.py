#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here

    diff = [a[i] - b[i] for i in range(len(a))]
    alice = sum(map(lambda x: 1 if x > 0 else 0, diff))
    bob = sum(map(lambda x: 1 if x < 0 else 0, diff))
    return [alice, bob]


if __name__ == '__main__':
    a = [5, 6, 7]
    b = [3, 6, 10]
    assert (compareTriplets(a, b) == [1, 1])