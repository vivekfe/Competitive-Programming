
# @Creation Date :  28/12/2022
# Description:      Multiprocessing

# import math
# import multiprocessing as mp
# import time
# results_a, results_b, results_c=[],[],[]
#
# def make_calculation_one(numbers):
#     for number in numbers:
#         results_a.append(math.sqrt(number**2))
#
# def make_calculation_two(numbers):
#     for number in numbers:
#         results_b.append(math.sqrt(number**3))
#
# def make_calculation_three(numbers):
#     for number in numbers:
#         results_c.append(math.sqrt(number**4))
#
# if __name__=="__main__":
#     number_list= list(range(5000000))
#     #Now we have processes
#     p1=mp.Process(target=make_calculation_one, args=(number_list,))
#     p2=mp.Process(target=make_calculation_two, args=(number_list,))
#     p3=mp.Process(target=make_calculation_three, args=(number_list,))
#     start= time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#     end= time.time()
#     print(f'Total time for three process to start {end-start}')
#     start= time.time()
#     make_calculation_one(number_list)
#     make_calculation_two(number_list)
#     make_calculation_three(number_list)
#     end= time.time()
#     print(f'Total time {end-start}')

# import time
# import multiprocessing
# import time
# s=[]
# c=[]
# def calc_square(numbers):
#     for n in numbers:
#         time.sleep(4)
#         s.append(n**2)
#
# def calc_cube(numbers):
#     for n in numbers:
#         time.sleep(4)
#         s.append(n**3)
#
# if __name__=="__main__":
#     arr=[2,3,8,9]
#     p1=multiprocessing.Process(target=calc_square, args=(arr,))
#     p2=multiprocessing.Process(target=calc_cube, args=(arr,))
#     start= time.time()
#     p1.start()
#     p2.start()
#     #below statements wait for both of these process to be over
#     p1.join()
#     p2.join()
#
#     end=time.time()
#     print(f'Total time {end-start}')

import time
import multiprocessing
import time
results=[]
def calc_square(numbers):
    global results
    for n in numbers:
        results.append(n**2)


if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square, args=(arr,))
    start= time.time()
    p1.start()
    p1.join()
    end=time.time()
    print(results)
    print(f'Total time {end-start}')
    # if we print results, it is empty. Every process has its own address space (virtual memory). Thus program
    #variables are not shared between two processes. You need to use IPC (Interprocess Communication) techniques
    #if you want to share data between two processes
