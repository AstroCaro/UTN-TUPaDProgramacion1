###################################################
################ ejercicio 1 ######################
###################################################
notas = [2, 4, 6, 8, 10, 5, 7, 9, 3, 1]

print("Notas ingresadas:")
for nota in notas:
    print(nota, end=" ")
print()

promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

###################################################
################ ejercicio 2 ######################
###################################################
productos = []
#Solicitamos al usuario que ingrese 5 nombres de productos
for i in range(0, 5):
    nombre = input("Ingrese el nombre del producto: ")
    productos.append(nombre)
    
#Mostramos la lista original
print("Productos ingresados:")
for producto in productos:
    print(producto, end=" ")
print()
    
#Mostramos la lista ordenada alfabéticamente
print("Productos ordenados alfabéticamente:")
productos_ordenados = sorted(productos)
for producto in productos_ordenados:
    print(producto, end=" ")
print()

#Eliminamos un producto especificado por el usuario
eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print(f"Producto '{eliminar}' eliminado.")
else:
    print(f"El producto '{eliminar}' no se encuentra en la lista.")
    
#Mostramos la lista actualizada
print("Lista actualizada de productos:")
for producto in productos:
    print(producto, end=" ")
print()

###################################################
################ ejercicio 3 ######################
###################################################

import random

numeros = []
numeros_pares = []
numeros_impares = []

# Generamos 15 números aleatorios entre 1 y 100
for i in range(15):
    numeros.append(random.randint(1, 100))
    
print("Números generados:")
for numero in numeros:
    print(numero, end=" ")

# Separamos números en pares e impares
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])
    else:
        numeros_impares.append(numeros[i])
        
# Mostramos resultados
print(f"Números pares tiene {len(numeros_pares)} elementos.")
print("Números pares:")
for numero in numeros_pares:
    print(numero, end=" ")
print()
print(f"Números impares tiene {len(numeros_impares)} elementos.")
print("Números impares:")
for numero in numeros_impares:
    print(numero, end=" ")
print()

###################################################
################ ejercicio 4 ######################
###################################################
datos = [1,3,5,3,7,1,9,5,3]
elementos_unicos = []

# Recorremos la lista y agregamos solo los elementos no repetidos
for dato in datos:
    if dato not in elementos_unicos:
        elementos_unicos.append(dato)

# Mostramos lista original y lista de elementos únicos
print("Lista original:")
for dato in datos:
    print(dato, end=" ")
print()

print("Elementos únicos:")
for elemento in elementos_unicos:
    print(elemento, end=" ")
print()

###################################################
################ ejercicio 5 ######################
###################################################
alumnos_presentes = [ "Luisa", "Carlos","Ana", "Miguel", "Sofia", "Diego", "Elena", "Marta"]
# Mostrar la lista inicial de alumnos presentes
print("Alumnos presentes en clase:")
for alumno in alumnos_presentes:
    print(alumno, end=" ")
print()

opcion = input("Elija una opción: \n"
               "1- Agregar un alumno \n"
               "2- Eliminar un alumno \n"
               "3- Salir \n")

# Loop hasta que el usuario decida salir
while opcion in ["1", "2"]:
    if opcion == "1":
        nuevo_alumno = input("Ingrese el nombre del alumno a agregar: ")
        alumnos_presentes.append(nuevo_alumno)
        print(f"Alumno '{nuevo_alumno}' agregado.")
    elif opcion == "2":
        eliminar_alumno = input("Ingrese el nombre del alumno a eliminar: ")
        if eliminar_alumno in alumnos_presentes:
            alumnos_presentes.remove(eliminar_alumno)
            print(f"Alumno '{eliminar_alumno}' eliminado.")
        else:
            print(f"El alumno '{eliminar_alumno}' no se encuentra en la lista.")
    
    print("Alumnos presentes en clase:")
    for alumno in alumnos_presentes:
        print(alumno, end=" ")
        
    opcion = input("\nElija una opción: \n"
                   "1- Agregar un alumno \n"
                   "2- Eliminar un alumno \n"
                   "Cualquier otra tecla para salir \n")
    
print("\nPrograma finalizado.")

###################################################
################ ejercicio 6 ######################
###################################################

lista = [1, 8, 3, 6, 5, 4, 7]
lista_rotada = []
# Rotar la lista hacia la derecha
for i in range(len(lista)):
    lista_rotada.append(lista[(i - 1) % len(lista)])

# Mostrar resultados
print("Lista original:")
for elemento in lista:
    print(elemento, end=" ")
print()
print("Lista rotada hacia la derecha:")
for elemento in lista_rotada:
    print(elemento, end=" ")
print()

###################################################
################ ejercicio 7 ######################
###################################################
# Lista de temperaturas mínimas y máximas para una semana de verano
temp = [
    [18,28],
    [15,21],
    [12,27],
    [18,34],
    [17,28],
    [19,30],
    [16,22]
]

# Calcular promedios
#promedio_minima = sum([temp[dia][0] for dia in range(len(temp))]) / len(temp)
#promedio_maxima = sum([temp[dia][1] for dia in range(len(temp))]) / len(temp)

minimas = [dia[0] for dia in temp]
maximas = [dia[1] for dia in temp]
promedio_minima = sum(minimas) / len(minimas)
promedio_maxima = sum(maximas) / len(maximas)
print(f"Promedio de temperaturas mínimas: {promedio_minima:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maxima:.2f}°C")

# Calcular día de mayor amplitud térmica
#amplitudes = [temp[dia][1] - temp[dia][0] for dia in range(len(temp))]
amplitudes = [dia[1] - dia[0] for dia in temp]
print(amplitudes)
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print(f"Día de mayor amplitud térmica: Día {dia_mayor_amplitud} con amplitud de {max(amplitudes)}°C")

###################################################
################ ejercicio 8 ######################
###################################################
#Lista de notas de 5 estudiantes en 3 materias
notas = [
    [10, 8, 9],
    [7, 6, 8],
    [9, 10, 10],
    [6, 5, 7],
    [8, 9, 8]    
]

# Calculamos el promedio de cada estudiante
for i, notas_est in enumerate(notas, start=1):
    print(f"Promedio del estudiante {i}: {sum(notas_est)/len(notas_est):.2f}")

# Calculamos el promedio de cada materia
for j, materia in enumerate(zip(*notas), start=1):
    print(f"Promedio de la materia {j}: {sum(materia)/len(materia):.2f}")
    
###################################################
################ ejercicio 9 ######################
###################################################
#Tablero Ta-te-ti como lista 3x3
tablero = [["-" for i in range(3)] for j in range(3)]

# Mostramos el tablero inicial
print("Tablero inicial:")
for fila in tablero:
    print(" | ".join(fila)) 

jugador = "X"
jugadas = 0
# Ciclo principal del juego
while jugadas < 9:
    fila = int(input(f"Jugador {jugador}, ingrese la fila (0-2): "))
    if fila < 0 or fila > 2:
        print("Fila inválida, intente nuevamente.")
        continue
    
    columna = int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
    if columna < 0 or columna > 2:
        print("Columna inválida, intente nuevamente.")
        continue
    # Verificamos si la posición está libre
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
        
        for fila in tablero:
            print(" | ".join(fila))
        
        # Cambiamos de jugador
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Posición ya ocupada, intente nuevamente.")
        continue
    
###################################################
################ ejercicio 10 #####################
###################################################
#Lista de ventas de 4 producto durante 7 días en una matriz 4x7
ventas = [
    [150000, 200000, 250000, 30000, 35000, 400000, 450000],  # Producto 1
    [120000, 220000, 320000, 420000, 520000, 620000, 720000],  # Producto 2
    [130000, 230000, 330000, 430000, 530000, 630000, 730000],  # Producto 3
    [140000, 240000, 340000, 440000, 540000, 640000, 740000]   # Producto 4
]
#Calculamos el total vendido por cada producto en la semana
for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    print(f"Total vendido por el Producto {i + 1} en la semana: ${total_producto}") 

#Calculamos el dia con mayores ventas totales
ventas_dia = [0] * 7  # Inicializamos una lista para almacenar las ventas diarias
for dia in range(7):
    for producto in range(4):
        ventas_dia[dia] += ventas[producto][dia]
dia_mayor_venta = ventas_dia.index(max(ventas_dia)) + 1
print(f"Día con mayores ventas totales: Día {dia_mayor_venta} con ventas de ${max(ventas_dia)}")

#Calculamos el producto más vendido en la semana
total_ventas_productos = [sum(ventas[i]) for i in range(4)]
producto_mas_vendido = total_ventas_productos.index(max(total_ventas_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} con ventas de ${max(total_ventas_productos)}")