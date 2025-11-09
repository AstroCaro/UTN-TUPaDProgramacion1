#ejercicio 1
EDAD_MINIMA = 18
edad = int(input("Ingrese su edad: ")) 
es_mayor = edad >= EDAD_MINIMA
if es_mayor:
    print("Es mayor de edad.")

#ejercicio 2
nota = float(input("Ingrese su nota (0-10): "))
aprobado = nota >= 6.0
if aprobado:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio 3
numero = int (input("Ingrese un número par: "))
es_par = numero % 2 == 0
if es_par:
    print("El número es par.")
else:
    print("Por favor, ingrese un número par.")
    
#ejercicio 4
edad = int(input("Ingresa tu edad: "))
if edad < 0:
    print("Edad inválida.")
elif edad < 12:
    print("Sos un niño.")
elif 12 <= edad < 18:
    print("Sos un adolescente.")
elif 18 <= edad < 30:
    print("Sos un adulto joven.")
else:
    print("Sos un adulto.")

#ejercicio 5
contrasena = input("Ingrese una contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres. ")

#ejercicio 6
consumo = float(input("Ingrese su consumo de energía eléctrica en kWh: "))
mensaje = ""
if consumo < 0:
    mensaje = "Consumo inválido."
elif consumo < 150:
    mensaje = "Consumo bajo"
elif 150 <= consumo <= 300:
    mensaje = "Consumo medio"
elif consumo > 300:
    mensaje = "Consumo alto"
    if consumo > 500:
        mensaje += " - Considere medidas de ahorro energético."
print(mensaje)

#ejercicio 7
frase = input("Ingrese una frase: ")
termina_vocal = frase[-1].lower() in 'aeiou'
if termina_vocal:
    frase = frase + "!"
print(frase)

#ejercicio 8
nombre = input("Ingresa tu nombre: ")
opcion = input("Ingresa una opción \n 1- Mayúsculas \n 2- Minúsculas \n 3- Primera letra en mayúscula ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida.")

#ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3:
    print("Muy leve")    
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#ejercicio 10
hemisferio = input("Ingrese el hemisferio dónde se encuentra \n"
                   "N- Norte \n"
                   "S- Sur \n"
                   ).strip().lower()

if hemisferio not in ["n", "s"]:
    print("Hemisferio no válido.")
    exit()

meses = [
    "enero","febrero","marzo","abril","mayo","junio",
    "julio","agosto","septiembre","octubre","noviembre","diciembre"
]
mes = input(
    "Ingrese el mes actual (ej.: enero, febrero, ...):\n> "
).strip().lower()
if mes not in meses:
    print("Mes no válido.")
    exit()

dia = int(input("Ingrese el día del mes: "))
if dia < 1 or dia > 31:
    print("Día no válido.")
    exit()

if hemisferio == "n":
    if ((mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20)):
        print("Invierno")
    elif ((mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20)):
        print("Primavera")
    elif ((mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20)):
        print("Verano")
    elif ((mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20)):
        print("Otoño")
elif hemisferio == "s":
    if ((mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20)):
        print("Invierno")
    elif ((mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20)):
        print("Primavera")
    elif ((mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20)):
        print("Verano")
    elif ((mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20)):
        print("Otoño")