#inputs for n and k
#n choose k = n! / (k! * (n-k)!)
n = int(input("Enter a number for n: "))
k = int(input("Enter a number for k: "))
#initialize result
result = 0

#set case for n = 0 or n=k
if k == 0 or k ==n:
    result = 1
else:
    numerator = 1
    denominator = 1
    for i in range(n,n-k,-1):
        numerator *= i

#computes factorial
    for i in range(1,k+1):
        denominator *= i
        result = numerator // denominator

print(f"The result of {n} choose {k} is {result}.")