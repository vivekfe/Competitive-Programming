
#Write a function that, for a given no n, finds a number p which is greater than or equal to n and is the smallest power of 2.
def getClosestPowerofTwo(n):
    count=0
    if (n & (n-1))==0 and n!=0:
        return n
    else:
        while n>0:
            n=n>>1
            count+=1
    return 1<<count

if __name__ == '__main__':
    print(getClosestPowerofTwo(0))
