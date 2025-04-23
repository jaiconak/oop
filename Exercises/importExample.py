# import functionExample
# import functionExample as func
from functionExample import hello,userInput,addition

hello()
# name = input("what is your name?")
# userInput(name)

num1 = int(input("num1: "))
num2 = int(input('num2: '))
total = addition(num1,num2)

print(f"Total is: {total}")