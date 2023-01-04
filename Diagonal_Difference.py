#!/bin/python3


import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    dim = len(arr[0])
    p_d, s_d = 0, 0
    for forward in range(dim):
        p_d = p_d + arr[forward][forward]
        s_d = s_d + arr[forward][dim - 1 - forward]
    return abs(p_d - s_d)

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
