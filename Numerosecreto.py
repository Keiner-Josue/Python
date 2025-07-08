Numero_Secreto = 159
averiguar = int(input("Averigua el numero secreto: "))
while averiguar != Numero_Secreto:
    if averiguar < Numero_Secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    averiguar = int(input("Sigue intentando: "))
print("¡Yepa gente, lo has adivinado!")