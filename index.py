from registro import registrar_usuario 
from consultar_usuario import consultar_usuario
def mostrar_menu():
    print("\n Biblioteca GrecoRomana")
    print("1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Consultar libros disponibles")
    print("4. consular préstamos")
    print("5. Libros extraviados")
    print("6. Deuda por exceder tiempo de préstamo")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1": 
            registrar_usuario()
        elif opcion == "2":
            consultar_usuario()
        elif opcion == "3":
            print("Función para consultar libros disponibles")
        elif opcion == "4":
            print("Función para consultar los prestamos del usuario")
        elif opcion == "5":
            print("Función para gestionar los libros extraviados")
        elif opcion == "6":
            print("Función para consultar deuda por exceder tiempo de préstamo")
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
