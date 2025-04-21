import rabrab

userInput = input("What size pizza do you want? [Choices : S, M ,L]")
try:
        if userInput.upper() == 'S':
            rabrab.smallPizza()
        if userInput.upper() == 'M':
            rabrab.mediumPizza()
        if userInput.upper() == 'L':
            rabrab.largePizza()

except ValueError:
    print ("Input must be s, m, or l!")
