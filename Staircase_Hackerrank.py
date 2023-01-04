#!/bin/python3



#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        s=" "*(n-i)+"#"*i
        print(s)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
