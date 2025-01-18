# Calculation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by 0 is not allowed."
    return a / b

def percentage(a, b):
    return a * b / 100

def power(a, b):
    return a ** b


# Function to evaluate a mathematical expression
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

    for operators_group in (('*', '/'), ('+', '-')):
        i = 0
        while i < len(tokens):
            if tokens[i] in operators_group:
                op = tokens[i]
                left = tokens[i - 1]
                right = tokens[i + 1]
                result = operators[op](left, right)
                tokens[i - 1:i + 2] = [result] 
                i -= 1  
            else:
                i += 1   
    return tokens[0]


# Function to display the operation history
def display_history(history):
    if not history:
        print("History is empty.")
    else:
        print("History of operations:")
        for entry in history:
            print(entry)


# Function to clear the operation history
def clear_history(history):
    history.clear()
    print("History has been cleared.")



# Main calculator function
def simple_calculator():
    history = []  

    while True:
        print("\n1. Basic Calculator\n2. Evaluate Expression\n3. View History\n4. Clear History\n5. Exit")
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
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '%':
                result = percentage(num1, num2)
            elif operator == '^':
                result = power(num1, num2)

            print(f"Result: {result}")
            history.append(f"{num1} {operator} {num2} = {result}")

        elif choice == '2':
            expression = input("Enter an expression (+, -, *, /): ")
            try:
                result = calculate_expression(expression)
                print(f"Result: {result}")
                history.append(f"{expression} = {result}")
            except Exception as e:
                print(f"Error processing expression: {e}")

        elif choice == '3':
            display_history(history)

        elif choice == '4':
            clear_history(history)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
# Program entry point
if __name__ == "__main__":
    simple_calculator()
