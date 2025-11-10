###################################################
################ ejercicio 1 ######################
###################################################

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

###################################################
################ ejercicio 2 ######################
###################################################

def saludar_usuario(nombre):
    return(f"Hola {nombre}!")
    
nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))

###################################################
################ ejercicio 3 ######################
###################################################

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("Le solicitaremos algunos datos personales.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

###################################################
################ ejercicio 4 ######################
###################################################

import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

#Programa principal
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")

###################################################
################ ejercicio 5 ######################
###################################################

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son equivalentes a {horas:.2f} horas.")

###################################################
################ ejercicio 6 ######################
###################################################

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#Programa principal
numero = int(input("Ingrese un número para conocer su tabla de multiplicar: "))
tabla_multiplicar(numero)

###################################################
################ ejercicio 7 ######################
###################################################

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = None
    return suma, resta, multiplicacion, division

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
if division is not None:
    print(f"División: {division}")
else:
    print("La división por cero no está definida.")

###################################################
################ ejercicio 8 ######################
###################################################

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

###################################################
################ ejercicio 9 ######################
###################################################

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f} °F")

###################################################
################ ejercicio 10 ######################
###################################################

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")