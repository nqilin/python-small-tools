# Simple Calculator in Python
# Supports basic arithmetic operations: +, -, *, /
# Author: nqilin
# Date: 2026 

def add(a, b):
    """Return the sum of a and b"""
    return a + b

def subtract(a, b):
    """Return the difference of a and b"""
    return a - b

def multiply(a, b):
    """Return the product of a and b"""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b, handle division by zero"""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("===== Simple Calculator =====")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is valid
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error! Please enter a valid number.")
            return

        # Perform calculation based on choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid input! Please select a valid operation.")

if __name__ == "__main__":
    main()
