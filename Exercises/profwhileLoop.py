# If the user is not either yes or no the scrfipt should keep asking for valid entry
entry = True
while entry:
    userInput = input ("enter yes or no as answer: ")
    if userInput.lower() == 'yes' or userInput.lower() == 'no':
        entry = False
    else:
        entry = True
        
print("farewell!")