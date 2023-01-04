
def gcd(a,b):
    if a%b==0:
        return a
    else:
        return gcd(a%b,a)

if __name__ == '__main__':
    print(gcd(40,30))