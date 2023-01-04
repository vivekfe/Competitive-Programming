#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    y=Counter(candles)
    return y.get(max(candles))

if __name__ == '__main__':
    candles= [4,4,1,3]
    result = birthdayCakeCandles(candles)
    assert result== 2

