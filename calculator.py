# Basic calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Options
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# User input
choice = input("Enter your choice (1/2/3/4): ")

# Make sure the choice is valid before asking for numbers
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    # Main logic
    if choice == '1':
        print("Addition:", add(num1, num2))
    elif choice == '2':
        print("Subtraction:", sub(num1, num2))
    elif choice == '3':
        print("Multiplication:", mul(num1, num2))
    elif choice == '4':
        print("Division:", div(num1, num2))
else:
    print("Error: Invalid input. Try again.")