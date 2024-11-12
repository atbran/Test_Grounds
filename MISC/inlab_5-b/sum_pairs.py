#this program iterates over two loops and finds the sum of the two numbers as it iterates over their ranges
#ie if num1 = 2 and num2 = 2, the program will output:
# 1+1 = 2 || 1+2 = 3 || 2+1 = 3 || 2+2 = 4

#gets input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#does the loop
for i in range(1,num1+1): #+1 needed to include the last number

    j = 1

    while j <= num2 :
        print(f"{i}, {j} = {i+j}")
        j+=1