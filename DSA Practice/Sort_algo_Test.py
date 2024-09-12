#This file would be used to calculate speed for sorting algorithms

import random
import numpy as np
import matplotlib.pyplot as plt
import time

#asks how many arrays to make
iterations = int(input("Enter number of iterations: "))

B_sort_yes = input("Would you like to use bubblesort? (Y/N) ")


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

#ChatGPT special
def quick_sort_GPT(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_GPT(left) + middle + quick_sort_GPT(right)
#found from https://stackoverflow.com/questions/18262306/quicksort-with-python
def quick_sort_Stack1(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort_Stack1(less)+equal+quick_sort_Stack1(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array



def measure_sort_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())  # Use arr.copy() to avoid sorting the same array twice
    end_time = time.perf_counter()
    return end_time - start_time




def __main__():
    bubble_sort_times = []
    merge_sort_times = []
    quick_GPT_sort_times = []
    quick_sort_Stack1_times = []
    array_lengths = []

    for i in range(iterations):
        array_length = int(input("Enter the length of the array (n^5): "))
        print("Input: " + str(array_length))
        array_length = array_length ** 5


        unsorted_array = gen_array(array_length)
        #print(unsorted_array)
        #print("\n")
        print("Array Length: " + str(array_length))
        print("Average: " + str(np.mean(unsorted_array)))

        # Measure Bubble Sort time
        if B_sort_yes.upper() == "Y":
            bubble_sort_time = measure_sort_time(bubble_sort, unsorted_array)
            bubble_sort_times.append(bubble_sort_time)
            print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")

        # Measure Merge Sort time
        merge_sort_time = measure_sort_time(merge_sort, unsorted_array)
        merge_sort_times.append(merge_sort_time)
        print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

        #Quick sort time GPT
        quick_GPT_sort_time = measure_sort_time(quick_sort_GPT, unsorted_array)
        quick_GPT_sort_times.append(quick_GPT_sort_time)
        print(f"GPT quick sort time: {quick_GPT_sort_time:.6f} seconds")

        # Quick sort time GPT
        quick_sort_Stack1_time = measure_sort_time(quick_sort_GPT, unsorted_array)
        quick_sort_Stack1_times.append(quick_sort_Stack1_time)
        print(f"Stack overflow quick sort time: {quick_sort_Stack1_time:.6f} seconds")

        array_lengths.append(array_length)

        print("\n")

    #Graph
    plt.figure(figsize=(12, 8))
    if B_sort_yes.upper() == "Y":
        plt.plot(array_lengths, bubble_sort_times, label="Bubble Sort", marker='o')
    plt.plot(array_lengths, merge_sort_times, label="Merge Sort", marker='o')
    plt.plot(array_lengths, quick_GPT_sort_times, label="Quick Sort GPT", marker='o')
    #plt.plot(array_lengths, quick_GPT_sort_times, label="Quick Sort GPT", marker='o')
    plt.plot(array_lengths, quick_sort_Stack1_times, label="Quick Sort STACK OVERFLOW", marker='o')
    #plt.plot(array_lengths, heap_sort_times, label="Heap Sort", marker='o')
    plt.xlabel('Array Size (n^5)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

__main__()