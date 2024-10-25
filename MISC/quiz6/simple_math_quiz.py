import random

def math_quiz():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    answer = num1 + num2
    print(f"What is \n   {num1} \n + {num2}? \n _______")
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        print("That is the right answer!")
    else:
        print(f"Sorry this is the wrong answer, the correct answer is {answer}.")

math_quiz()