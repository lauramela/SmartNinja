number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")
operation = input("Please enter the calculation you want to perform (+, -, * or /): ")

if operation == "+":
    print(int(number1) + int(number2))
elif operation == "-":
    print(int(number1) - int(number2))
elif operation == "*":
    print(int(number1) * int(number2))
elif operation == "/":
    print(int(number1) / int(number2))
else:
    print("Sorry, I don't recognize this operator.")