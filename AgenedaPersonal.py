contactos = {
    "Juan": "3145678897",
    "Maria": "3156789901",
    "Pedro": "3167890123",
    "Ana": "3178901234",
    "Luis": "3189012345",
    "Laura": "3190123456",
    "Carlos": "3201234567",
}

while True:
    print("\n1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        numero = input("Número del contacto: ")
        contactos[nombre] = numero
        print(f"Contacto {nombre} agregado.")
    elif opcion == "2":
        print("\nLista de contactos:")
        for nombre, numero in contactos.items():
            print(f"{nombre}: {numero}")
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        if buscar in contactos:
            print(f"{buscar}: {contactos[buscar]}")
        else:
            print("Contacto no encontrado.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
