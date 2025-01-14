def add(a,b):
    return a+b

def subtract (a,b):
    return a-b  
  
def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return("Error. la division par 0 interdite")
    return a/b

def calculator():
    while True:
        choix = input("Voulez-vous utiliser + .-.*./.:  ")
        if choix in ["+","-"," *","/"]:
            try:
             num1 = float(input("Entrez le premier nombre: "))
             num2 = float(input("Entrez le deuxième nombre: "))
            except(ValueError):
                print("Erreur")
                return 
        
        
            if choix == '+':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choix == '-':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choix == '*':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choix == '/':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
         print("Erreur. Choix invalide. ")
         return
        continue

if __name__ == "__main__":
    calculator()


    

    
