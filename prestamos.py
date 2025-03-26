import json
from datetime import datetime

USUARIOS_FILE = "usuarios.json"
PRESTAMOS_FILE = "prestamos.json"

def cargar_datos(archivo):
    """Carga datos desde un archivo JSON."""
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

def usuario_existe(usuario_id):
    """Verifica si el usuario con el ID existe en `usuarios.json`."""
    usuarios = cargar_datos(USUARIOS_FILE)
    return any(usuario["ID"] == usuario_id for usuario in usuarios)

def contar_prestamos_usuario(usuario_id, prestamos):
    """Cuenta los préstamos activos de un usuario por su ID."""
    return sum(1 for p in prestamos if p["usuario_id"] == usuario_id and p["estado"] == "Activo")

def realizar_prestamo(usuario_id, titulo_libro, libros_disponibles):
    """Registra un préstamo si el usuario existe y tiene menos de 2 préstamos activos."""
    
    # Verificar si el usuario existe
    if not usuario_existe(usuario_id):
        print(f"❌ El usuario con ID {usuario_id} no está registrado.")
        return

    prestamos = cargar_datos(PRESTAMOS_FILE)

    # Verificar si el usuario ya tiene 2 préstamos activos
    if contar_prestamos_usuario(usuario_id, prestamos) >= 2:
        print(f"❌ El usuario con ID {usuario_id} ya tiene 2 préstamos activos. No puede solicitar más.")
        return

    # Buscar si el libro está disponible
    libro_encontrado = next((libro for libro in libros_disponibles if libro["titulo"].lower() == titulo_libro.lower()), None)

    if not libro_encontrado:
        print("❌ El libro no está disponible en la biblioteca.")
        return

    # Registrar el préstamo
    fecha_prestamo = datetime.today().strftime('%Y-%m-%d')
    nuevo_prestamo = {
        "usuario_id": usuario_id,
        "titulo": titulo_libro,
        "fecha_prestamo": fecha_prestamo,
        "estado": "Activo"
    }

    prestamos.append(nuevo_prestamo)  
    guardar_datos(PRESTAMOS_FILE, prestamos) 

    print(f"✅ ¡Préstamo registrado con éxito!\n📖 Libro: {titulo_libro}\n🆔 Usuario ID: {usuario_id}\n📅 Fecha: {fecha_prestamo}")

def consultar_prestamos(usuario_id):
    """Consulta y muestra los préstamos activos de un usuario por su ID."""
    
    # Verificar si el usuario existe
    if not usuario_existe(usuario_id):
        print(f"❌ El usuario con ID {usuario_id} no está registrado.")
        return

    prestamos = cargar_datos(PRESTAMOS_FILE)

    prestamos_usuario = [p for p in prestamos if p["usuario_id"] == usuario_id and p["estado"] == "Activo"]

    if prestamos_usuario:
        print(f"\n📕 Préstamos activos del usuario ID {usuario_id}:")
        for prestamo in prestamos_usuario:
            print(f"📖 {prestamo['titulo']} (Fecha de préstamo: {prestamo['fecha_prestamo']})")
    else:
        print(f"❌ El usuario con ID {usuario_id} no tiene préstamos activos.")

