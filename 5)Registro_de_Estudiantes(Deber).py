# Diccionario global para almacenar estudiantes y sus calificaciones
estudiantes = {}

# Función para agregar un estudiante
def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    notas = []
    while True:
        entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado con éxito!")

# Función para mostrar todos los estudiantes y sus notas
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    
    print("Estudiantes registrados:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {notas} (Promedio: {sum(notas)/len(notas) if len(notas) > 0 else 0})")
        
def Actualizar_promedio():
    nombre = input("Escriba el nombre del estudiante: ")
    if nombre in estudiantes:
        notas = []
        while True:
            entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
            try:
                nota = float(entrada)
                notas.append(nota)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        estudiantes[nombre] = notas
        print(f"Notas de {nombre} actualizadas con éxito!")
    else:
        print("Estudiante no encontrado")

# Función para calcular el promedio general de todas las notas
def promedio_general():
    total_notas = 0
    total_estudiantes = 0
    for notas in estudiantes.values():
        total_notas += sum(notas)
        total_estudiantes += len(notas)
    
    if total_estudiantes == 0:
        return 0
    
    return total_notas / total_estudiantes

def Buscar():
    nombre = input("ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
         print(f"El estuadinte {nombre} posee las siguientes notas: {estudiantes[nombre]}")
    else:
        print("Estudiante no encontrado")

# Función principal
def main():
    while True:
        print("")
        print("-" * 17 ,"Menú del Sistema de Registro", "-" * 17)
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar promedio general")
        print("4. Actualizar")
        print("5. Buscar estudiante")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        print("-" * 65)
        print("")
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            promedio = promedio_general()
            print(f"El promedio general de todas las calificaciones es: {promedio}")
        elif opcion == '4':
            Actualizar_promedio()
        elif opcion == '5':
            Buscar()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()