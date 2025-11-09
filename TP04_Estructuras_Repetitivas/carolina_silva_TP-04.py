#ejercicio 1
for i in range(101):
    print(i)

#ejercicio 2
numero = int(input("Ingrese un número: "))
aux = abs(numero)

if numero == 0:
    cant = 1

cant = 0
 
while aux > 0:
    aux = aux // 10
    cant += 1
    
print(f"El número {numero} tiene {cant} dígitos.")

#ejercicio 3
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

suma = 0

if (num_1 >= num_2):
    num_1, num_2 = num_2, num_1

for i in range(num_1 + 1, num_2):
    suma += i

print(f"La suma de los números entre {num_1} y {num_2} es: {suma}")

#ejercicio 4
suma = 0
num = int(input("Ingrese un número (0 para salir): "))

while num != 0:
    suma += num
    num = int(input("Ingrese un número (0 para salir): "))
    
print(f"La suma acumulada es: {suma}")

#ejercicio 5
import random
num = random.randint(0, 9)
cant_intentos = 1

print("Adivina el número entre 0 y 9")
adivina = int(input("Ingrese su número: "))
while adivina != num:
    print("Número incorrecto, intente nuevamente.")
    adivina = int(input("Ingrese su número: "))
    cant_intentos += 1
    
print(f"¡Felicidades! Adivinaste el número {num} en {cant_intentos} intentos.")

#ejercicio 6
for i in range(100, -1, -2):
    print(i)
    
#ejercicio 7
num = int(input("Ingrese un número entero positivo: "))
if num < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    suma = 0
    for i in range(num+1):
        suma += i
    print(f"La suma de los números desde 0 hasta {num} es: {suma}")

#ejercicio 8
CANT_NUMEROS = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(CANT_NUMEROS):
    num = int(input(f"Ingrese el número {i + 1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num >= 0:
        positivos += 1
        
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")

#ejercicio 9
CANT_NUMEROS = 10
suma = 0

for i in range(CANT_NUMEROS):
    num = int(input(f"Ingrese el número {i + 1}: "))
    suma += num
    
print(f"La suma total de los {CANT_NUMEROS} números ingresados es: {suma}")
print(f"La media es: {suma / CANT_NUMEROS:.2f}")

#ejercicio 10
num = int(input("Ingrese un número entero: "))
num_invertido = 0
aux = abs(num)
while aux > 0:
    num_invertido = num_invertido * 10 + (aux % 10)
    aux = aux // 10

print(f"El número invertido es: {num_invertido if num >= 0 else -num_invertido}")