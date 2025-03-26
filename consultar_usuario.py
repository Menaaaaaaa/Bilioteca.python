import json

USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON, si existe."""
    try:
        with open(USUARIOS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

def consultar_usuario():
    """Busca un usuario por su ID y muestra Nombre, Correo y Teléfono, sin el ID."""
    usuarios = cargar_usuarios()

    if not usuarios:
        print("\n❌ No hay usuarios registrados.")
        return

    try:
        usuario_id = int(input("🔍 Ingrese el ID del usuario a consultar: ")) 
    except ValueError:
        print("\n⚠️ Error: El ID debe ser un número.")
        return

    for usuario in usuarios:
        if usuario["ID"] == usuario_id:
            print("\n✅ Información del usuario:")
            print(f"👤 Nombre: {usuario['Nombre']}")
            print(f"📧 Correo: {usuario['Correo']}")
            print(f"📞 Teléfono: {usuario['Teléfono']}")
            return
    
    print("\n❌ Usuario no encontrado. Verifique el ID ingresado.")

