
def division(a,b):
    counter = 0
    sign = -1 if (a<0)^(b<0) else 1
    b = abs(b)
    a = abs(a)
    while b>=a:
        b=b-a
        counter+=1
        #division(a,b)
    return sign*counter, b


b=100
a=2

x=5
y=-43

print(f'Quotient  of {a} and {b} is {division(a,b)[0]} and remainder is {division(a,b)[1]}')
print(f'Quotient  of {x} and {y} is {division(x,y)[0]} and remainder is {division(x,y)[1]}')
