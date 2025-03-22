import json

USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    #Carga los usuarios desde el archivo JSON, si existe.
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Si no hay archivo, devuelve una lista vacía

def consultar_usuario():
    """Busca un usuario por su ID numérico y muestra solo el ID."""
    usuarios = cargar_usuarios()

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    try:
        usuario_id = int(input("Ingrese el ID del usuario a consultar: "))  # Convertimos a número
    except ValueError:
        print("\nError: El ID debe ser un número.")
        return

    for usuario in usuarios:
        if usuario["ID"] == usuario_id:
            print(f"\nID: {usuario['ID']}")  # Muestra solo el ID
            return
    
    print("\nUsuario no encontrado. Verifique el ID ingresado.")
