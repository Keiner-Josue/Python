numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))
operacion = int(input("1. Sumar, 2. Restar, 3. Multiplicar, 4. Dividir: "))

if operacion == 1:
    suma = (numeroUno + numeroDos)
    print(f"La suma entre: {numeroUno} y {numeroDos} es: {suma}")
elif operacion == 2:
    resta = (numeroUno - numeroDos)
    print(f"La resta entre: {numeroUno} y {numeroDos} es: {resta}")
elif operacion == 3:
    multiplicar = (numeroUno * numeroDos)
    print(f"La resta entre: {numeroUno} y {numeroDos} es: {multiplicar}")
elif operacion == 4:
    dividir = (numeroUno/numeroDos)
    print(f"La resta entre: {numeroUno} y {numeroDos} es: {dividir }")