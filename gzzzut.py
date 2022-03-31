import gzzzut_funciones as Red
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Gzzzut")


if os.path.isfile(nombre+".user"):
    #   Esto lo hacemos si ya habia un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user", "r")
    nombre = archivo_usuario.readline()
    edad = archivo_usuario.readline()
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m)*100)
    num_amigos = archivo_usuario.readline()
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    zodiaco = archivo_usuario.readline()
    estado = archivo_usuario.readline()
#   Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()


else:
    #   En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    num_amigos = Red.obtener_lista_amigos()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    zodiaco = Red.obtener_zodiaco()
    estado = ""
    muro = []


print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado)


opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        mensaje = Red.obtener_mensaje()
        Red.checar_mensaje(nombre, None, mensaje)
    elif opcion == 2:
        mensaje = Red.obtener_mensaje()
        for i in range((len(num_amigos))-(len(num_amigos)-1)):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.checar_mensaje(nombre, nombre_amigo, mensaje)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado)
    elif opcion == 4:
        nombre = Red.obtener_nombre()
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        num_amigos = Red.obtener_lista_amigos()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        zodiaco = Red.obtener_zodiaco()
        estado = Red.mostrar_muro(estado)
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado)
    elif opcion == 5:
        nuevo_nombre = input("¿A que perfil quieres cambiar?")
        (nombre, edad, estatura_m, estatura_cm, num_amigos, sexo, pais, zodiaco, estado) = Red.cambiar_usuario(nuevo_nombre)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        archivo_usuario = open(nombre + ".user", "w")
        archivo_usuario.write(nombre + "\n")
        archivo_usuario.write(str(edad) + "\n")
        archivo_usuario.write(str(estatura_m + estatura_cm / 100) + "\n")
        archivo_usuario.write(str(num_amigos) + "\n")
        archivo_usuario.write(sexo + "\n")
        archivo_usuario.write(pais + "\n")
        archivo_usuario.write(zodiaco + "\n")
        archivo_usuario.write(estado)
        # Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
        archivo_usuario.close()
        print("Archivo", nombre + ".user", "guardado")

print("Gracias por usar Gzzzut, ha sido divertido. ¡Hasta pronto!")
