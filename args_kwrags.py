#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:         "Vivek SRIVASTAVA <vivek2.srivastava@hsbc.com>"
# @Creation Date :  27/12/2022
# Description:      <>

#################################################################################
# Raw way to use
def my_sum(a,b):
    return a+b

print(my_sum(2,3))

#################################################################################
# This arg iterator is not a list, it is a tuple
# Args way to use, good way to pass positional arguments
def my_sum(*args):
    print(type(args))
    return sum(args)

print(my_sum(2,3))

##################################################################################

def my_sum(**kwargs):
    sum=0
    for i in kwargs.values():
        sum=sum+i
    return sum
print(my_sum(a=1,b=2))

##################################################################################

def mix_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

mix_arguments(1,2,3, KEYONE="1", KEYTWO="2")

##################################################################################

import sys
sys.argv[0] #prints out the file name
