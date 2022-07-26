# Implement a calculator with basic functionalities

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    if (y == 0):
        print('float division by zero')
        return "None"
    return x / y

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if choice in ('+', '-', '*', '/', '#'):
        if choice == '#':
            print("Done. Terminating")
            exit()
   

        num1 = input("Enter first number: ")
        if num1.isnumeric():
            print(int(num1))
        else:
            print (num1)
            continue
    
        
        num2 = input("Enter second number: ")
        if num2.isnumeric():
            print(int(num2))
        elif num2 == '#':
            print(num2)
            print("Done. Terminating")
            exit()
        else:
            print (num2)
            continue
            
            
        if choice == '+':
            print(float(num1), "+", float(num2), "=", float(add(int(num1), int(num2))))
    
        elif choice == '-':
            print(float(num1), "-", float(num2), "=", float(subtract(int(num1), int(num2))))

        elif choice == '*':
            print(float(num1), "*", float(num2), "=", multiply(int(num1), int(num2)))
    
        elif choice == '/':
            print(float(num1), "/", float(num2), "=", divide(int(num1), int(num2)))