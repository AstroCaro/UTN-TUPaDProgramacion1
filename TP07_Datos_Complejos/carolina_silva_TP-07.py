###################################################
################ ejercicio 1 ######################
###################################################

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Agregar precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


###################################################
################ ejercicio 2 ######################
###################################################

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Agregar precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


###################################################
################ ejercicio 3 ######################
###################################################

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Agregar precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

frutas = list(precios_frutas.keys())
print(frutas)


###################################################
################ ejercicio 4 ######################
###################################################

# Crear un diccionario para almacenar contactos telefónicos
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero
# Consultar un número telefónico por nombre
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print("El contacto no existe.")

###################################################
################ ejercicio 5 ######################
###################################################

#Contar la cantidad de veces que aparece cada palabra en una frase ingresada por el usuario.
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
print(f"Palabras únicas {palabras_unicas}")
print(f"Recuento: {conteo_palabras}")

###################################################
################ ejercicio 6 ######################
###################################################

notas_dic = {}
for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    suma = 0
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {alumno}: "))
        notas.append(nota)
        suma += nota
    promedio = suma / 3
        
    notas_tupla = tuple(notas)
    notas_dic[alumno] = (notas_tupla), f"{promedio:.2f}"
    print(f"Notas y promedio de {alumno}: {notas_dic[alumno]}")
    
###################################################
################ ejercicio 7 ######################
###################################################

# Operaciones de conjuntos
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107, 108}
aprobados_ambos = parcial1.intersection(parcial2)
print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {aprobados_solo_uno}")
aprobados_al_menos_uno = parcial1.union(parcial2)
print(f"Estudiantes que aprobaron al menos un parcial: {aprobados_al_menos_uno}")

###################################################
################ ejercicio 8 ######################
###################################################

def mostrar_menu():
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("Cualquiera otra tecla para salir")

def consultar_stock(productos):
    producto = input("Ingrese el nombre del producto a consultar: ")
    if producto in productos:
        print(f"El stock de {producto} es: {productos[producto]}")
    else:
        print(f"El producto {producto} no existe en el inventario.")

def agregar_stock(productos):
    producto = input("Ingrese el nombre del producto al que desea agregar stock: ")
    if producto in productos:
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if cantidad > 0:
            productos[producto] += cantidad
            print(f"Stock actualizado: {producto} → {productos[producto]}")
        else:
            print("La cantidad debe ser positiva.")
    else:
        print(f"El producto {producto} no existe en el inventario.")
        
def agregar_producto(productos):
    producto = input("Ingrese el nombre del nuevo producto: ")
    if producto not in productos:
        cantidad = int(input("Ingrese la cantidad inicial: "))
        if cantidad >= 0:
            productos[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")
        else:
            print("La cantidad debe ser no negativa.")
    else:
        print(f"El producto '{producto}' ya existe.")

productos_stock = {'harina': 10, 'azúcar': 5, 'sal': 8, 'aceite': 12}
mostrar_menu()
opcion = input("Seleccione una opción:")


while opcion in ['1', '2', '3']:
    if opcion == '1':
        consultar_stock(productos_stock)
    elif opcion == '2':
        agregar_stock(productos_stock)
    elif opcion == '3':
        agregar_producto(productos_stock)
    
    mostrar_menu()
    opcion = input("Seleccione una opción:")
print("Saliendo del programa. ¡Vuelva pronto!")

###################################################
################ ejercicio 9 ######################
###################################################

#Ingreso de eventos en una agenda.
agenda = {}
continuar = True
while continuar:
    dia = input("Ingrese el día del evento: ")
    hora = input("Ingrese la hora del evento: ")
    evento = input("Ingrese el nombre del evento: ")
    agenda[(dia, hora)] = evento
    continuar = input("¿Desea agregar otro evento? (s/n): ").lower() == 's'
    
print("Agenda de eventos:")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}") 
    
#Permití consultar qué actividad hay en cierto día y hora.
consultar_dia = input("Ingrese el día a consultar: ")
consultar_hora = input("Ingrese la hora a consultar: ")
evento_consultado = agenda.get((consultar_dia, consultar_hora))
if (consultar_dia, consultar_hora) in agenda:
    print(f"El evento es: {agenda[(consultar_dia, consultar_hora)]}")
else:
    print("No hay eventos para ese día y hora.")

###################################################
################ ejercicio 10 #####################
###################################################

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima",
    "Venezuela": "Caracas",    
}
# Invertir el diccionario
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original (países a capitales):")
print(paises_capitales)
print("Diccionario invertido (capitales a países):")
print(capitales_paises)