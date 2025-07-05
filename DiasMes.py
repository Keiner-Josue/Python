mes = input("Escribe el nombre del mes: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    print(f"{mes.capitalize()} tiene 31 días.")
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    print(f"{mes.capitalize()} tiene 30 días.")
elif mes == "febrero":
    print(f"{mes.capitalize()} tiene 28 días, o 29 en año bisiesto.")
else:
    print("Mes no válido. Por favor, escribe un mes correcto.")
