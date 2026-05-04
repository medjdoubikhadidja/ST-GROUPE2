import json

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b

def save_operation(operation):
    try:
        with open("../json/history.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(operation)

    with open("../json/history.json", "w") as file:
        json.dump(data, file, indent=4)

print("=== Calculatrice ===")

while True:
    print("\n1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choice = input("Choisir une opération: ")

    if choice == "5":
        print("Au revoir !")
        break

    a = float(input("Entrer le premier nombre: "))
    b = float(input("Entrer le deuxième nombre: "))

    if choice == "1":
        result = add(a, b)
        op = f"{a} + {b} = {result}"
    elif choice == "2":
        result = subtract(a, b)
        op = f"{a} - {b} = {result}"
    elif choice == "3":
        result = multiply(a, b)
        op = f"{a} * {b} = {result}"
    elif choice == "4":
        result = divide(a, b)
        op = f"{a} / {b} = {result}"
    else:
        print("Choix invalide")
        continue

    print("Résultat:", result)
    save_operation(op)
