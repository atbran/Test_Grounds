#this uses elements of dynamic programming.

num_arr = [0,1]

def fib(num):
    if num < 0:
        return 0
    elif num < len(num_arr):
        return num_arr[num]
    else:
        num_arr.append(fib(num-1) + fib(num-2))
        return num_arr[num]

num = int(input("Input a number: "))

print(fib(num))