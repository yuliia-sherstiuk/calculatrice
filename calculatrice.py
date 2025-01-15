# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Function to calculate the percentage of the first number based on the second
def percentage(a, b):
    return a * b / 100

# Function to raise the first number to the power of the second
def power(a, b):
    return a ** b

# Function to get the user's operation choice
def get_user_choice():
    return input("Choose an operation (+  -  *  /  %  ^ ) or 'Q' to quit: ").strip()

# Function to get two numbers from the user
def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return None, None

# Function to perform the operation based on the user's choice
def perform_operation(choice, num1, num2):
    if choice == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '-':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '*':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '/':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '%':
        print(f"{num1} * {num2}/100 = {percentage(num1, num2)}")
    elif choice == '^':
        print(f"{num1} ** {num2} = {power(num1, num2)}")

# Main function to run the calculator
def main():
    while True:
        choice = get_user_choice()
        if choice == "Q":
            print("Exiting the program. Goodbye!")
            break
        elif choice in ["+", "-", "*", "/", "%", "^"]:
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                perform_operation(choice, num1, num2)
        else:
            print("Error! Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()


    

    
