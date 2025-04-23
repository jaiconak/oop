'''
Write a script that will take two integers and give the sum of those two int. 
  7- write a script that will take user's age and tell if there are eligible to vote or not. 
'''

# Todo 1

print ("Prob 1: ")
userInput1 = int(input("Insert num1: "))
userInput2 = int(input("Insert num2: "))
add =  (userInput1 + userInput2)
print (f"The total of the two numbers are: {add}")

entrance = input ("Would you like to proceed? ")
if entrance.upper() == 'YES':
  ageInput = int(input("Whats your age? "))
  if ageInput >= 21:
      print ("You're unc level now")
  else:
      print("baby fr")

else:
  print ("okay bye :p")
  
    
    
    