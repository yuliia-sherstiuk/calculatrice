def add(a,b):
    return a+b

def subtract (a,b):
    return a-b  
  
def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        print("Error. la division par 0 interdite")
    return a/b

choix = input("Voulez-vous utiliser + .-.*./.:  ")
num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))

if choix == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
elif choix == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choix == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choix == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
 

print()


    
