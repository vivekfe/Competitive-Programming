# find the number of lattice points on the circumference of the circle of radius n
import math


def lattice_points(radius):
    l= [(i,j) for i in range(radius+1) for j in range(radius+1) if i*i+j*j==radius*radius]
    # for i in l:
    #     if i[0]!=0 and i[1]!=0:
    #         l.append((-i[0],-i[1]))
    #         l.append((i[0], -i[1]))
    #         l.append((-i[0], i[1]))
    #     if i[0]!=0 and i[1]==0:
    #         l.append((-i[0], i[1]))
    #     if i[0]==0 and i[1]!=0:
    #         l.append((i[0], -i[1]))
    return l

if __name__=='__main__':
    radius=5
    y=lattice_points(radius)
    print(f'Total number of lattice points on the radius of circle {radius} is {y}')