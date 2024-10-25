#this program calculates the fibonacci sequence up to a certain number


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
num = int(input("Input a number: "))

print(fib(num))