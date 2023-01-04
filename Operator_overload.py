# @Creation Date :  27/12/2022
# Description:      Operator overload

class Vector:
    def __init__(self, x,y):
        self.x= x
        self.y=y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __repr__(self):
        return f'Vector\'s values are {self.x} and {self.y}'

    def __call__(self, *args, **kwargs):
        print("Hello I was Called")

v1=Vector(20,30)
v2=Vector(30,40)
v3=v1+v2
print(v3.x, v3.y)
print(v3)
v3()

# use __repr__ if you want to have a user friendly representation of the vector class
