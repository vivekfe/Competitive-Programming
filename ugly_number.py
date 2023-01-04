
def max_division(a,b):
    while a%b==0:
        a=a/b
    return a

def isUgly(num):
    num = max_division(num, 2)
    num = max_division(num, 3)
    num = max_division(num, 5)
    return 1 if num==1 else 0

def getNthUglyNo(num):
    count=1 # 1 as ugly number
    i=1
    while count<num+1:
        i += 1
        if isUgly(i):
            count+=1
    return i

no=getNthUglyNo(150)
print(no)

