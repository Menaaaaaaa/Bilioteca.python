libros_disponibles = [
    {"titulo": "La Ilíada", "autor": "Homero", "año": "Siglo VIII a.C."},
    {"titulo": "La Odisea", "autor": "Homero", "año": "Siglo VIII a.C."},
    {"titulo": "Eneida", "autor": "Virgilio", "año": "Siglo I a.C."},
    {"titulo": "Las Metamorfosis", "autor": "Ovidio", "año": "Siglo I d.C."},
    {"titulo": "Antígona", "autor": "Sófocles", "año": "Siglo V a.C."},
    {"titulo": "Edipo Rey", "autor": "Sófocles", "año": "Siglo V a.C."},
    {"titulo": "Medea", "autor": "Eurípides", "año": "Siglo V a.C."},
    {"titulo": "Electra", "autor": "Eurípides", "año": "Siglo V a.C."},
    {"titulo": "Los trabajos y los días", "autor": "Hesíodo", "año": "Siglo VIII a.C."},
    {"titulo": "Historia", "autor": "Heródoto", "año": "Siglo V a.C."},
    {"titulo": "Anábasis", "autor": "Jenofonte", "año": "Siglo IV a.C."},
    {"titulo": "La República", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Ética a Nicómaco", "autor": "Aristóteles", "año": "Siglo IV a.C."},
    {"titulo": "Las Bacantes", "autor": "Eurípides", "año": "Siglo V a.C."},
    {"titulo": "Prometeo encadenado", "autor": "Esquilo", "año": "Siglo V a.C."},
    {"titulo": "Los siete contra Tebas", "autor": "Esquilo", "año": "Siglo V a.C."},
    {"titulo": "Lisístrata", "autor": "Aristófanes", "año": "Siglo IV a.C."},
    {"titulo": "Las Nubes", "autor": "Aristófanes", "año": "Siglo IV a.C."},
    {"titulo": "Las Aves", "autor": "Aristófanes", "año": "Siglo IV a.C."},
    {"titulo": "Las Ranas", "autor": "Aristófanes", "año": "Siglo IV a.C."},
    {"titulo": "El Banquete", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Apología de Sócrates", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Fedón", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Timeo", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Poética", "autor": "Aristóteles", "año": "Siglo IV a.C."},
    {"titulo": "Política", "autor": "Aristóteles", "año": "Siglo IV a.C."},
    {"titulo": "Retórica", "autor": "Aristóteles", "año": "Siglo IV a.C."},
    {"titulo": "Las Leyes", "autor": "Platón", "año": "Siglo IV a.C."},
    {"titulo": "Las Historias", "autor": "Tucídides", "año": "Siglo V a.C."},
    {"titulo": "Vidas Paralelas", "autor": "Plutarco", "año": "Siglo I d.C."},
    {"titulo": "De la naturaleza de las cosas", "autor": "Lucrecio", "año": "Siglo I a.C."},
    {"titulo": "Ab urbe condita", "autor": "Tito Livio", "año": "Siglo I a.C."},
    {"titulo": "Las Cartas", "autor": "Séneca", "año": "Siglo I d.C."},
    {"titulo": "Las Meditaciones", "autor": "Marco Aurelio", "año": "Siglo II d.C."},
    {"titulo": "Las Sátiras", "autor": "Juvenal", "año": "Siglo II d.C."},
    {"titulo": "Los Anales", "autor": "Tácito", "año": "Siglo I d.C."},
    {"titulo": "Germania", "autor": "Tácito", "año": "Siglo I d.C."},
    {"titulo": "El Arte de Amar", "autor": "Ovidio", "año": "Siglo I a.C."},
    {"titulo": "La Consolación de la Filosofía", "autor": "Boecio", "año": "Siglo VI d.C."},
    {"titulo": "La Guerra de las Galias", "autor": "Julio César", "año": "Siglo I a.C."},
    {"titulo": "Las Confesiones", "autor": "San Agustín", "año": "Siglo IV d.C."},
    {"titulo": "La Ciudad de Dios", "autor": "San Agustín", "año": "Siglo V d.C."}
]


def buscar_libro(criterio=""):
    #Busca libros por título o autor. Si no se proporciona criterio, muestra todos los libros disponibles.
    criterio = criterio.strip().lower()  

    if not criterio:  # Si el usuario no ingresa nada, muestra todos los libros
        return libros_disponibles  

    resultados = [libro for libro in libros_disponibles if 
                  criterio in libro["titulo"].lower() or 
                  criterio in libro["autor"].lower()]

    return resultados if resultados else "No se encontraron libros con ese criterio."

