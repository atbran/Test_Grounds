#This script will be used to show how different searching algorithms function in different O(n) complexities.
#I hope to also add a feature which graphs and shows the actual time to calculate the search times along with the
#size of the array/list.

import time
import matplotlib.pyplot as plt
import random


#asks how many arrays to make
iterations = int(input("Enter number of iterations: "))



#generate nlength sorted array to use algorithm on
def generate_sorted_array(n):
    return [i for i in range(n)]
#linear search
def lin_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#binary search algo

def binary_search(arr,target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#below are random search algos I either found online or made for fun


def hybrid_search(arr,target):
    return binary_search(arr,target) if len(arr) >= 10**5 else lin_search(arr,target)
    #This does binary search only if the array is greater than 10^5 else it does lin search

def measure_time(search_function, arr, target):
    start_time = time.perf_counter() #perf counter is more accurate ala gpt suggestion
    result = search_function(arr, target)
    end_tme = time.perf_counter()
    return result, end_tme - start_time

#main function below
def __main__():
    for i in range(int(iterations)):
        #Ask user for array size for each iteration
        n = int(input("Enter size of array (5^n): "))
        n = 5**n

        if n >= 10**9:
            print(f"Your array of size {n} is too big!")
            continue
        arr = generate_sorted_array(n)
        print(f"Array of size {n} is generated")

        #set the target to search
        #note: must not be lazy and just do //2, it must truly be a random value!
        target = random.randint(0,n-1)
        print(f"Target is {target}")

        # Measure time for each algorithm
        linear_result, linear_time = measure_time(lin_search, arr, target)
        binary_result, binary_time = measure_time(binary_search, arr, target)
        eclectic_result, eclectic_time = measure_time(hybrid_search, arr, target)

        # Display search results and timings
        print(f"Linear Search Result: {linear_result} | Time: {linear_time:.10f} seconds")
        print(f"Binary Search Result: {binary_result} | Time: {binary_time:.10f} seconds")
        print(f"Eclectic Search Result: {eclectic_result} | Time: {eclectic_time:.10f} seconds")

    #graph results

    plt.figure(figsize=(12, 8))
    #plt.plot()

#let er rip!!
__main__()