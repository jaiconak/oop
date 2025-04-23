trigger1 = True
trigger2 = True

while trigger1:
    answer = input("Do you want to leave?")
    if answer.upper() == 'NO':
        print ("very well")
        trigger1 = True
    if answer.upper() == 'YES':
        print ("Proceed with the riddle...")
        trigger1 = False
while trigger2:
    name = input("To pass this TIME LOOP... you must enter the greatest ENGINEER!!!: ")
    if name.upper() == 'JAICO':
            trigger2 = False
    else:
        pass