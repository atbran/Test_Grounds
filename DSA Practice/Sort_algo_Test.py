#This file would be used to calculate speed for sorting algorithms

import random
import numpy as np
import matplotlib as plt
import time

#asks how many arrays to make
iterations = int(input("Enter number of iterations: "))


#Generate array
def gen_array(array_length):
    array = [_ for _ in  range(array_length)]
    #shuffles the array
    random.shuffle(array)
    return array

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    #print("Sorted Array: " + str(array) + "\n")

def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

def measure_sort_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())  # Use arr.copy() to avoid sorting the same array twice
    end_time = time.perf_counter()
    return end_time - start_time




def __main__():
    bubble_sort_times = []
    merge_sort_times = []
    array_lengths = []

    for i in range(iterations):
        array_length = int(input("Enter the length of the array (n^5): "))
        array_length = array_length ** 5

        unsorted_array = gen_array(array_length)
        #print(unsorted_array)
        #print("\n")
        print("Array Length: " + str(array_length))
        print("Average: " + str(np.mean(unsorted_array)))
        bubble_sort(unsorted_array)
        merge_sort(unsorted_array)
        # Measure Bubble Sort time
        bubble_sort_time = measure_sort_time(bubble_sort, unsorted_array)
        bubble_sort_times.append(bubble_sort_time)
        print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")

        # Measure Merge Sort time
        merge_sort_time = measure_sort_time(merge_sort, unsorted_array)
        merge_sort_times.append(merge_sort_time)
        print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

        array_lengths.append(array_length)
__main__()