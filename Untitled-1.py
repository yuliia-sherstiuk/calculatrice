def demander_nombre (message):
    while True:
        try:
            return float (input(message))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre valide.")

def demander_operation ():
    operations = ['+', '-', '*', '/', '^']
    while True:
        operations = input(f"Entrez le type d'opération ({'/'.join(operations)}): ").strip()
    if operations in operations:
        return operations
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
     
    
        
