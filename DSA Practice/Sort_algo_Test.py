#This file would be used to calculate speed for sorting algorithms

import random
from array import array
from random import randrange

import matplotlib as plt
import time

#asks how many arrays to make
iterations = int(input("Enter number of iterations: "))

#user input


#Generate array
def gen_array(array_length):
    array = [_ for _ in  range(array_length)]
    random.shuffle(array)
    return array




def __main__():
    array_length = int(input("Enter the length of the array (n^5): "))
    array_length = array_length ** 5

    unsorted_array = gen_array(array_length)
    print(unsorted_array)

__main__()