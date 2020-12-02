print("\t\t\tDigiCalc v1.0")
print("\t\t\tAuthor: rly0nheart")

# Python program for simple calcu
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
# Function to subtract two number
def subtract(num1, num2):
    return num1 - num2
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


if __name__ == '__main__':
    # Main loop
    while True:
        print('''\n\nSelect An Operator\n
        1. Division
        2. Multiplication
        3. Addition
        4. Subtraction''')
        # Take input from the user
        strn = "is equal to"
        userinp = int(input("\n"))
        num1 = int(input( "Enter first number(s):\n"))
        num2 = int(input("Enter second number(s):\n\n"))
 
        if userinp == 1:
            print(num1, "➗ ", num2, strn, divide(num1,num2))
        elif userinp == 2:
            print(num1, "✖️ " , num2, strn, multiply(num1, num2))
        elif userinp == 3:
              print(num1, "➕ " , num2, strn, add(num1, num2))
        elif userinp == 4:
                print(num1, "➖ " , num2, strn, subtract(num1, num2))
        else:
            print ( " ⚠️UNKNOWN OPERATOR⚠️\n " )
            print("SYNTAX ERROR🚫⚠️ ")
    
        print("do you want to calculate again?")
        userinp = str(input().lower())
        if  "yes" in userinp:
            continue
        else:
        	print(exit)
        	break