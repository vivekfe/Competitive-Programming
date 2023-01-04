# @Creation Date :  28/12/2022
# Description:      Examples on Multithreading

# Notes https://www.youtube.com/watch?v=3dEPY3HiPtI

# thread = a flow/sequence of execution. Like a separate order of instructions
#           both thread and process are independent sequences of execution
#           however each thread takes a turn running to achieve concurrency
#           GIL = Global Interpreter Lock
#           allows only one thread to hold the control of the Python interpreter

# cpu bound = program/ tasks spends most of its time waiting for internal events (CPU intense)
#            use multiprocessing

# io bound = program/tasks spends most of its time waiting for external events (user inputs, web scraping)
#            use multithreading

# thread takes turns while one of them is sitting idle

import threading
import time   # print the list of all the threads currently running using the enumerate function

# for example we are running late for morning and we have three different tasks to be completed before we leave for school or work
# eat brakfast, coffee, study last minute

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish study")

# eat_breakfast()
# drink_coffee()
# study()

# the way it works with assumption is that once you eat breakfast, then only you drink coffee and only after finishing coffee,
# we finish our study, so it is not concurrent but it is sequential
# however as humans, we tend to all three together

# in this case one thread is responsible for running three fnctions, what if we create 3 different threads
if __name__=="__main__":
    start= time.time()
    x=threading.Thread(target=eat_breakfast, args=())
    x.start()
    y=threading.Thread(target=drink_coffee, args=())
    y.start()
    z=threading.Thread(target=study, args=())
    z.start()

    end = time.time()

    # performance counter simply measures the performance of what it is responsible for
    # however we can achieve the thread synchronization such that main thread waits for the respective thread and then move on to it's
    # sequencial instructions

    x.join()
    y.join()
    z.join()

    print(f'All {threading.active_count()} threads finished in {end-start}')   # count the number of threads running currently in the backgreound
    print(threading.enumerate())
    print(time.perf_counter())

