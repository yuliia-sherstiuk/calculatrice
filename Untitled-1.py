

def demander_nombre(message):
    """Demande un nombre à l'utilisateur et gère les erreurs d'entrée."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre valide.")

def demander_operation():
    """Demande une opération à l'utilisateur et vérifie sa validité."""
    operations = ['+', '-', '*', '/', '^']
    while True:
        operation = input(f"Entrez le type d'opération ({'/'.join(operations)}): ").strip()
        if operation in operations:
            return operation
        else:
            print("Opération invalide. Veuillez choisir parmi les opérations proposées.")

def effectuer_calcul(nombre1, nombre2, operation):
    """Effectue le calcul selon les paramètres donnés et gère les erreurs."""
    try:
        if operation == '+':
            return nombre1 + nombre2
        elif operation == '-':
            return nombre1 - nombre2
        elif operation == '*':
            return nombre1 * nombre2
        elif operation == '/':
            if nombre2 == 0:
                raise ZeroDivisionError("Division par zéro non autorisée.")
            return nombre1 / nombre2
        elif operation == '^':
            return nombre1 ** nombre2
    except ZeroDivisionError as e:
        print(e)
        return None

def main():
    """Programme principal de la calculatrice."""
    print("Bienvenue dans la calculatrice !")
    while True:
        nombre1 = demander_nombre("Entrez le premier nombre : ")
        nombre2 = demander_nombre("Entrez le deuxième nombre : ")
        operation = demander_operation()

        resultat = effectuer_calcul(nombre1, nombre2, operation)
        if resultat is not None:
            print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

        continuer = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").strip().lower()
        if continuer != 'oui':
            print("Merci d'avoir utilisé la calculatrice. À bientôt !")
            break

if __name__ == "__main__":
    main()