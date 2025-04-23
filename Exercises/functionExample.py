def hello ():
    print ("Hello world")

def userInput(user):
    print(f"Hello {user}")


# try:
#     userInput("Jaico")
# except:
#     print("Must input string value in the function")
    
def addition(x,y):
    total = x + y
    return total


def commands (cmd):
    import os 
    os.system(cmd)

# commands('top')

def clearScreen():
    import os       # showing importance of global variables so it can be used everywhere
    os.system('clear')


# def main():

#     try:
#         x = int(input("Enter number to be added: "))
#         y = int(input("Enter number to be added: "))
    
#         total= addition(x,y)
#         print (f"The total number is: {total}")
        
#     except ValueError:
#         print("Must be numbers")
