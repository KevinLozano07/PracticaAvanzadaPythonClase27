# Diccionario global para almacenar el inventario
inventario = {}

# Función para agregar productos
def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    if producto in inventario:  # Bifurcación doble
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado con éxito!")

def actualizar():
    producto = input("Qué producto desea actualizar: ")
    
    if producto in inventario:  
        cantidad = int(input(f"Ingrese la nueva cantidad para {producto}: "))
        inventario[producto] = cantidad  
        print(f"El producto {producto} ahora tiene {cantidad} unidades.")
    else:
        print("Este producto no está dentro del inventario.")


# Función para eliminar productos
def eliminar_producto():
    producto = input("Ingresa el nombre del producto a eliminar: ")
    if producto in inventario:  # Bifurcación simple
        del inventario[producto]
        print(f"Producto {producto} eliminado con éxito!")
    else:
        print(f"El producto {producto} no está en el inventario.")

# Función para mostrar el inventario
def mostrar_inventario():
    if len(inventario) == 0:  # Bifurcación doble
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for producto, cantidad in inventario.items():  # Bucle for
            print(f"{producto}: {cantidad} unidades")

# Función principal que controla el menú
def main():
    while True:  # Bucle while
        print("")
        print("-" * 27, "Menú de Inventario", "-" * 27)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Actualizar productos")
        print("5. Salir")
        print("")
        opcion = input("Elige una opción: ")
        print("-" * 74)
        print("")
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            actualizar()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()