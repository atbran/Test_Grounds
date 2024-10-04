import time

array = [3,5,2,8,4,1,0]

print(str(array) + "\n")
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        print(array)
        time.sleep(.5)
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    #print("Sorted Array: " + str(array) + "\n")

bubble_sort(array)