# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-08-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""

import time
from time import strftime
from datetime import datetime


#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
                
        if args:
            func(args)       # main_function
        else:
            func()

        end_time = time.time()
        result = f'{func.__name__} - END: {strftime("%H:%M:%S")}, {(end_time-start_time).__round__(2)} seconds'
        print(result)

    return wrapper


#*********************************************************************
# Current time for reference
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(0.1)
    print(name)

@print_process
def mid_sleeping():
    time.sleep(2)

@print_process
def long_sleeping():
    time.sleep(4)

short_sleeping("so sleepy")

mid_sleeping()

long_sleeping()
