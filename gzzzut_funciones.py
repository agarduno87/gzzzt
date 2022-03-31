import os


def mostrar_bienvenida():
    print()
    print("Hola, bienvenido a Gzzzut, tu nueva red social...")
    print(" ... ")
    print(""" .--.                          .-. 
    : .--'                        .' `.
    : : _ .---. .---. .---. .-..-.`. .'
    : :; :`-'_.'`-'_.'`-'_.': :; : : : 
    `.__.'`.___;`.___;`.___;`.__.' :_;""")
    print("Suscríbete, es gratis y segura.")
    print()


def obtener_nombre():
    nombre = str(input("Para empezar, dime cómo te llamas. "))
    print("Hola ", nombre, ", bienvenido a esta nueva red social llamada Gzzzut.")
    return nombre


def obtener_edad():
    ano = int(input("Para preparar tu perfil, dime en qué año naciste: "))
    edad = 2021 - ano
    print("Oh!, tú tienes ", edad, " años. Ahi la llevas.")
    return edad


def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros: "))
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    return metros, centimetros


def obtener_sexo():
    sexo = input("Bien, por favor dime qué sexo eres. Selecciona ('M' ó 'm') o ('F' ó 'f'): ")
    while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
        sexo = input("Por favor, ingresa tu sexo (M ó m=Masculino, F ó f=Femenino): ")
    return sexo


def obtener_pais():
    pais = input("Continuando, es importante conocer el país desde donde nos escribes: ")
    return pais


def obtener_zodiaco():
    zodiaco = input("Ahora por favor escribe tu signo zodiacal: ")
    return zodiaco


def obtener_lista_amigos():
    linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos


def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_lista_amigos()
    s = obtener_sexo()
    p = obtener_pais()
    z = obtener_zodiaco()
    es = mostrar_muro()
    return n, e, em, ec, na, s, p, z, es


def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado):
    print()
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Amigos:   ", num_amigos)
    print("Tu sexo es: ", sexo)
    print("Nos escribes desde: ", pais)
    print("Tu caballero del zodiaco es: ", zodiaco)
    print("Tu estado es: ", estado)
    print("--------------------------------------------------")
    print()


def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  5. Selecciona el usuario al que quieres cambiar")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 5:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion


def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje


def checar_mensaje(emisor, receptor, dice):
    print("--------------------------------------------------")
    if receptor is None:
        print(emisor, "dice:", dice)
    else:
        print(emisor, "dice:", "@"+receptor, dice)
    print("--------------------------------------------------")


# Muestra los mensajes recibidos
def mostrar_muro(muro):
    print("------ MURO ("+str(len(muro))+" mensajes) ---------")
    for dice in muro:
        print(dice)
    print("--------------------------------------------------")

# Publica un mensaje en el timeline personal y en el de los amigos


def publicar_mensaje(emisor, receptor, dice, muro):
    print("--------------------------------------------------")
    print(emisor, "dice:", dice)
    print("--------------------------------------------------")
#   Agrega el mensaje al final del timeline local
    muro.append(dice)
#   Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in receptor:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user", "w")
            archivo.write(emisor+":"+dice+"\n")
            archivo.close()


def existe_archivo(ruta):
    return os.path.isfile(ruta)


def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user", "r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m)*100)
    num_amigos = len(num_amigos)
    sexo = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    zodiaco = archivo_usuario.readline().rstrip()
    estado = archivo_usuario.readline().rstrip()
#   Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensajes = archivo_usuario.readline().rstrip()
    while mensajes != "":
        muro.append(mensajes)
        mensajes = archivo_usuario.readline().rstrip()
#   Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado, muro


def escribir_usuario(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado):
    archivo_usuario = open(nombre+".user", "w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    archivo_usuario.write(";".join(num_amigos) + "\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(zodiaco+"\n")
    archivo_usuario.write(estado+"\n")
# Escribe el 'timeline' en el archivo, a continuación del último estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
# Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()


def cambiar_usuario(nombre):
    if existe_archivo(nombre + ".user"):
        archivo_usuario = open(nombre+".user", "r")
        nombre = archivo_usuario.readline().rstrip()
        edad = int(archivo_usuario.readline())
        estatura = float(archivo_usuario.readline())
        estatura_m = int(estatura)
        estatura_cm = int((estatura - estatura_m)*100)
        num_amigos = int(len(archivo_usuario.readline()))
        sexo = archivo_usuario.readline().rstrip()
        pais = archivo_usuario.readline().rstrip()
        zodiaco = archivo_usuario.readline().rstrip()
        estado = archivo_usuario.readline().rstrip()
        archivo_usuario.close()
        return nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado
    else:
        crear = obtener_datos()
        return crear