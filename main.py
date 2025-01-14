
def addition():
	answer = y + z
	print(f"{y} + {z} = {answer}")

def soustraction():
	answer = y - z
	print(f"{y} - {z} = {answer}")
def multiplication():
	answer = y * z
	print(f"{y} * {z} = {answer}")

def division():
   if y == 0 or z == 0 :
      print("non vraiment pas 0 sa se divise pas")
   else:
      try:
      
         answer = y / z
         print(f"{y} / {z} = {answer}")
      except ValueError:
         print("Frenchement non")

   


print("A. Addition")
print("B. Soustraction")
print("C. Multiplication")
print("D. Division")
print("E. Quitter")

choix = input("Entrez votre choix : ")


y = int(input("Veuillez entrer un nombre :  "))
z = int(input("Veuillez entrer le deuxième nombre :"))


if choix == "A" or choix == "a" :
   addition()
elif choix == "b" or choix == "B" :
   soustraction()
elif choix == "c" or choix == "C" :
   multiplication()
elif choix == "D" or choix == "d" :
    division()
elif choix == "E" or  choix == "e" :
   print("pas fait")
