from registro import registrar_usuario 
from consultar_usuario import consultar_usuario
from consultaLibro import buscar_libro, libros_disponibles
from prestamos import realizar_prestamo, consultar_prestamos

def mostrar_menu():
    print("\n===== Biblioteca GrecoRomana =====")
    print("1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Consultar libros disponibles")
    print("4. Realizar préstamos")
    print("5. Consultar préstamos")
    print("6. Salir")
    print("=" * 35) 

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if not opcion.isdigit():  # Verifica si es un número
            print("❌ Entrada no válida. Ingrese un número entre 1 y 6.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            consultar_usuario()
        elif opcion == 3:
            criterio = input("Ingrese el título o autor del libro que busca (o deje en blanco para ver todos): ").strip()
            resultados = buscar_libro(criterio)

            if isinstance(resultados, list) and resultados:
                print("\n📚 Libros encontrados:")
                for libro in resultados:
                    print(f"📖 {libro['titulo']} | ✍️ Autor: {libro['autor']} | 📅 Año: {libro['año']}")
            else:
                print("❌ No se encontraron libros con ese criterio.")

        elif opcion == 4: 
            usuario_id = int(input("Ingrese el ID del usuario: "))
            titulo_libro = input("Ingrese el título del libro a prestar: ")
            realizar_prestamo(usuario_id, titulo_libro, libros_disponibles)

        elif opcion == 5:
            usuario_id = int(input("Ingrese el ID del usuario: "))
            consultar_prestamos(usuario_id)
        
        elif opcion == 6:
            print("Gracias por visitar a la Bilioteca GrecoRomana, estás saliendo del sistema... ¡Hasta luego!👋 ")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
