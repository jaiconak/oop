print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill_amt = 0

def smallPizza () :
    bill_amt = 15
    if pepperoni == "N":
        bill_amt = bill_amt
    elif pepperoni == "Y":
        bill_amt +=2
    if extra_cheese  == "N":
        bill_amt = bill_amt
    elif extra_cheese  == "Y":
        bill_amt +=1
        print(f"Your final bill is: ${bill_amt}.")

def mediumPizza():
    bill_amt = 20
    if pepperoni == "N":
        bill_amt = bill_amt
    elif pepperoni == "Y":
         bill_amt += 3
    if extra_cheese == "N":
        bill_amt = bill_amt
    elif extra_cheese == "Y":
        bill_amt += 1
        print(f"Your final bill is: ${bill_amt}.")

def largePizza():
    bill_amt = 25
    if pepperoni == "N":
        bill_amt = bill_amt
    elif pepperoni == "Y":
        bill_amt += 3
    if extra_cheese == "N":
        bill_amt = bill_amt
    elif extra_cheese == "Y":
        bill_amt += 1
    print(f"Your final bill is: ${bill_amt}.")
  
def main ():
    userInput = input("What size pizza do you want? [Choices : S, M ,L]")
    try:
        if userInput.upper() == 'S':
            smallPizza()
        if userInput.upper() == 'M':
            mediumPizza()
        if userInput.upper() == 'L':
            largePizza()
    except ValueError:
        print ("Input must be s, m, or l!")

if __name__ == "___main__":
    main ()

