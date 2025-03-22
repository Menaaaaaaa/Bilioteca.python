import json

USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    #Carga los usuarios desde el archivo JSON, si existe.
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def guardar_usuarios(usuarios):
    #Guarda la lista de usuarios en el archivo JSON.
    with open(USUARIOS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

def obtener_nuevo_id(usuarios):
    #Obtiene el siguiente ID secuencial.
    if usuarios:
        ultimo_id = max(usuario["ID"] for usuario in usuarios)
        return ultimo_id + 1
    return 1  # Si no hay usuarios, empezamos con ID = 1

def registrar_usuario():
    #Solicita datos del usuario, le asigna un ID secuencial y los guarda.
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese su nombre completo: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")

    usuarios = cargar_usuarios()
    usuario_id = obtener_nuevo_id(usuarios)

    usuario = {
        "ID": usuario_id,
        "Nombre": nombre,
        "Correo": correo,
        "Teléfono": telefono
    }

    # Agregar y guardar usuario
    usuarios.append(usuario)
    guardar_usuarios(usuarios)

    print("\nUsuario registrado con éxito:")
    for clave, valor in usuario.items():
        print(f"{clave}: {valor}")

    return usuario["ID"] # Retorna solo el ID del usuario
