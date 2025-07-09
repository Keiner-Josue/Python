usuarios = {
    "keiner": "python123",
    "maria": "1234"
}

nombre = input("Usuario: ")
clave = input("Contraseña: ")

if nombre in usuarios and clave == usuarios[nombre]:
    print("¡Acceso correcto!")
else:
    print("Acceso denegado.")
