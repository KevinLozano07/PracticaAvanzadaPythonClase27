# Definimos una variable global para el umbral
umbral = 5.0
# Función para pedir las notas
def pedir_notas():
    notas = []
    while True:
        nota = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        print("")
        if nota.lower() == 'fin':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            print("")
    return notas

# Función para filtrar notas por el umbral
def filtrar_notas(notas):
    notas_filtradas = []
    for nota in notas:
        if nota >= umbral:  # Bifurcación simple
            notas_filtradas.append(nota)
    return notas_filtradas

#Nota exclidas por no cumplir la cantidad segun el umbral
def notas_excluidas(notas):
    notas_exc = 0
    for nota in notas:
        if nota < umbral:
            notas_exc += 1
    return notas_exc       

# Función para calcular el promedio
def calcular_promedio(notas):
    if len(notas) == 0:  # Bifurcación doble
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return promedio

# Función principal
def main():
    notas = pedir_notas()
    notas_filtradas = filtrar_notas(notas)
    promedio = calcular_promedio(notas_filtradas)
    excluidas = notas_excluidas(notas)
    print("-" * 80)
    print(f"La cantidad de notas que fueron excluida es de: {excluidas} notas")
    print("")
    print(f"El promedio de las notas que están por encima del umbral ({umbral}) es: {promedio}")
    
    
# Llamamos a la función principal
print("")
main()
print("-" * 80)
print("")