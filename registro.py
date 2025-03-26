import json

USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON, si existe."""
    try:
        with open(USUARIOS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

def guardar_usuarios(usuarios):
    """Guarda la lista de usuarios en el archivo JSON."""
    with open(USUARIOS_FILE, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)

def obtener_nuevo_id(usuarios):
    """Obtiene el siguiente ID secuencial."""
    if usuarios:
        ultimo_id = max(usuario["ID"] for usuario in usuarios)
        return ultimo_id + 1
    return 1  # Si no hay usuarios, el primer ID será 1

def registrar_usuario():
    """Solicita datos del usuario, le asigna un ID secuencial y los guarda."""
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese su nombre completo: ").strip()
    correo = input("Ingrese su correo electrónico: ").strip()
    telefono = input("Ingrese su número de teléfono: ").strip()

    # Cargar usuarios y obtener nuevo ID
    usuarios = cargar_usuarios()
    usuario_id = obtener_nuevo_id(usuarios)

    # Crear usuario
    usuario = {
        "ID": usuario_id,
        "Nombre": nombre,
        "Correo": correo,
        "Teléfono": telefono
    }

    # Guardar usuario
    usuarios.append(usuario)
    guardar_usuarios(usuarios)

    # Mensaje de confirmación con el ID asignado
    print(f"\n✅ ¡Registro exitoso! \n  {nombre} le corresponde el ID: {usuario_id} 🎉")

    return usuario["ID"]  # Retorna el ID asignado

