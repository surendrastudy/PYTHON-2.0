#in-built functions  ==  int() str()
#Module functions
#user-defined functions



#Module functions  ----  related function and related file store in same file

# import math
# print(dir(math))

# from math import *

from math import sqrt
print(sqrt(4)) # square root

#user-defined functions


# def function_name(parameters): ----  Syntax
#     //do something



# def print_sum(a , b):
#     print(a + b)

# print_sum(1,2)


def print_sum(a=8 , b=2):
    print(a + b)

print_sum()