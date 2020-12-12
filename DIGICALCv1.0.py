# simple calculator(Digicalc ver-1.0)
# Author: rlyonheart
# Twitter: rly0nheart
# Github: rlyonheart
# ©2021



# for loop that prints a number pattern(it's not important')
rows = 15
for i in range(1, rows):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")
# for loop ends here


#import color module termcolor
import sys
from termcolor import colored, cprint

print(colored("\t\t    DiGiCALC v1.0.1(cmd line)   ", 'blue', attrs=['bold','underline']))

# Function for adding two numbers

def add(num1, num2):

    return num1 + num2

# Function for subtracting two numbers

def subtract(num1, num2):

    return num1 - num2

# Function for multiplying two numbers

def multiply(num1, num2):

    return num1 * num2

# Function for dividing two numbers

def divide(num1, num2):

    return num1 / num2





if __name__ == '__main__':

    # Main loop

    while True:

        print(colored("\n\n\tCH00SE OPERATOR:\n\n",'yellow',attrs=['bold','underline']))

        cprint('''        1. ➗

        2. ✖️ 

        3. ➕

        4. ➖''','white',attrs=['bold'])

        # Take input from the user

        strn = colored("is equal to" ,'magenta',attrs=['bold'])

        userinp = int(input("\n\n\t==> "))

        num1 = int(input("Enter first number(s):\n\n==>  "))

        num2 = int(input("Enter second number(s):\n\n==>  "))


 
        if userinp == 1:
        	print("\n",num1, "➗", num2," ", strn , divide(num1,num2))

        elif userinp == 2:
        	print("\n",num1, "✖️", num2," ", strn , multiply(num1, num2))

        elif userinp == 3:
        	print("\n",num1, "➕", num2," ", strn, add(num1, num2))

        elif userinp == 4:
        	print("\n",num1 , "➖", num2," ", strn , subtract(num1, num2))

        else:
        	cprint("⚠️INVALID OPERATOR⚠️  ",'white','on_red',attrs=['bold'])
        	cprint("SYNTAX ERROR🚫⚠️   ",'white','on_red',attrs=['bold'])

    

        print(colored("\n\nWould You Like To Calculate Again?\n",'white',attrs=['bold']))

        userinp = str(input().lower())

        if  "yes" in userinp:

            continue

        else:
        	print(colored(exit,'white','on_red'))
        	break