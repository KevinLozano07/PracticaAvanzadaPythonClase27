import random

# Variables globales
intentos_max = 0

print("")
print("-" * 80)
Ni = int(input("Desde que numero se inicia: "))
Nf = int(input("Hasta que numero se llega: "))
print("")
intentos_max = int(input("Cuantos intentos desea tener para adivinar el numero: "))
print("-" * 80)

numero_secreto = random.randint(Ni, Nf)

# Función para pedir una adivinanza
def pedir_adivinanza():
    try:
        return int(input(f"Adivina el número (entre {Ni} y {Nf}): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

# Función principal del juego
def juego_adivinanza():
    intentos = 0
    while intentos < intentos_max:  # Bucle while
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:  # Bifurcación doble
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print("")
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            
            break
    else:
        print("")
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")
        

# Función principal para iniciar el juego
def main():
    print("")
    print("*" * 30, "Descubre el numero", "*" * 30)
    juego_adivinanza()
    print("*" * 80)
    print("")
# Llamamos a la función principal
main()