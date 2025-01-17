#Calculation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error. Division by 0 is not allowed."
    return a / b

def percentage(a, b):
    return a * b / 100

def power(a, b):
    return a ** b


def calculate_expression(expression):
    operators = {'+': add, '-': subtract, '*': multiply, '/': divide}
    tokens = []
    num = ''

    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        elif char in operators:
            if num:
                tokens.append(float(num))
                num = ''
            tokens.append(char)
    if num:
        tokens.append(float(num))

    # Perform operations in order of precedence
    for op in ('*', '/', '+', '-'):
        while op in tokens:
            idx = tokens.index(op)
            left = tokens[idx - 1]
            right = tokens[idx + 1]
            result = operators[op](left, right)
            tokens[idx - 1:idx + 2] = [result]

    return tokens[0]

def simple_calculator():
    
  
    while True:
        print("1. Basic Calculator\n2. Evaluate Expression\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            operator = input("Choose an operation (+, -, *, /, %, ^): ")
            if operator not in ['+', '-', '*', '/', '%', '^']:
                print("Invalid operator.")
                continue
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Error: Invalid input.")
                continue

            if operator == '+':
                print(f"Result: {add(num1, num2)}")
            elif operator == '-':
                print(f"Result: {subtract(num1, num2)}")
            elif operator == '*':
                print(f"Result: {multiply(num1, num2)}")
            elif operator == '/':
                print(f"Result: {divide(num1, num2)}")
            elif operator == '%':
                print(f"Result: {percentage(num1, num2)}")
            elif operator == '^':
                print(f"Result: {power(num1, num2)}")

        elif choice == '2':
            expression = input("Enter an expression ( +, -, *, /): ")
            try:
                result = calculate_expression(expression)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error processing expression: {e}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simple_calculator()
