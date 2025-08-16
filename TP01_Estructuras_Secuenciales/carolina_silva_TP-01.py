# ejercicio 1
print("Hola Mundo")

# ejercicio 2
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}!")

# ejercicio 3
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")
lugarResidencia = input("Introduce tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}.")

# ejercicio 4
radio = input("Ingresa el radio de un círculo: ")
pi = 3.14159
perimetro = 2 * pi * float(radio)
area = pi * float(radio) ** 2
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")

# ejercicio 5
segundos = input("Ingresa un número de segundos: ")
horas = int(segundos) // 3600
print(f"{segundos} segundos son {horas} horas.")

# ejercicio 6
numero = input("Ingresa un número: ")
print(f"{numero} x 1 = {int(numero) * 1}")
print(f"{numero} x 2 = {int(numero) * 2}")
print(f"{numero} x 3 = {int(numero) * 3}")
print(f"{numero} x 4 = {int(numero) * 4}")
print(f"{numero} x 5 = {int(numero) * 5}")
print(f"{numero} x 6 = {int(numero) * 6}")
print(f"{numero} x 7 = {int(numero) * 7}")
print(f"{numero} x 8 = {int(numero) * 8}")
print(f"{numero} x 9 = {int(numero) * 9}")
print(f"{numero} x 10 = {int(numero) * 10}")

# ejercicio 6 (con bucle for)
numero = input("Ingresa un número: ")
for i in range(1, 11):
  print(f"{numero} x {i} = {int(numero) * i}")

# ejercicio 7
num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")

num1 = int(num1)
num2 = int(num2)

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# ejercicio 8
altura = input("Ingresa tu altura en metros: ")
peso = input("Ingresa tu peso en kilogramos: ")

imc = float(peso) / (float(altura) ** 2)

print(f"Tu IMC es: {imc:.2f}")

# ejercicio 9
tempCelsius = input("Ingresa la temperatura en grados Celsius: ")
tempFahrenheit = (9/5 * float(tempCelsius) + 32 )

print(f"La temperatura en grados Fahrenheit es: {tempFahrenheit}")

# ejercicio 10
num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")
num3 = input("Ingresa el tercer número: ")
promedio = (int(num1) + int(num2) + int(num3)) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")