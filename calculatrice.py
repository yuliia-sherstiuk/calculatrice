# calculer l'addition de deux nombres
def addition(x,y):
    return x + y

# calculer la soustraction de deux nombres
def soustraction(x,y):
    return x - y

# calculer la multiplication de deux nombres
def multiplication(x,y):
    return x * y

# calculer la division de deux nombres
def division(x,y):
    return x / y

print (" Les opperation possibles :\n1 : Addition\n2 : Soustraction \n3 : Multiplication \n4 : Division \n5 : Quitter ")

while True :
    choix = int(input("Entrez votre choix :"))
    
    if choix == 5:
            print("Au revoir")
            break
        
    num1 = float(input("Veuillez entrez le premier nombre:"))
    num2 = float(input("Veuillez entrez le deuxième nombre:"))
        
    if choix == 1:
            print(num1, "+", num2, "=", addition(num1,num2))
            
    elif choix == 2:
            print(num1, "-", num2, "=", soustraction(num1,num2)) 
        
    elif choix == 3:
            print(num1, "*", num2, "=", multiplication(num1,num2)) 
            
    elif choix == 4:
            if num2 == 0:
                raise ZeroDivisionError("Erreur : Division par zéro non permise.")
            else :
                print(num1, "/", num2, "=", division(num1,num2))  
                
    else :
        print("Erreur : Entrer des nombres valides.")
