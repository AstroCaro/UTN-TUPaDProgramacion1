###################################################
################ ejercicio 1 ######################
###################################################

print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")

###################################################
################ ejercicio 2 ######################
###################################################

print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")
    
    
print("Leyendo con readlines():")
with open("productos.txt", "r") as archivo:
    archivo.readline()  # Saltar la primera línea de encabezados
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")

###################################################
################ ejercicio 3 ######################
###################################################

def lectura_archivo():
    print("Leyendo con readlines():")
    with open("productos.txt", "r") as archivo:
        archivo.readline()  # Saltar la primera línea de encabezados
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
            
            
print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")
    
lectura_archivo()
        
        
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

print("Agregando nueva línea con append()")
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

lectura_archivo()

###################################################
################ ejercicio 4 ######################
###################################################

def lectura_archivo():
    print("Leyendo con readlines():")
    with open("productos.txt", "r") as archivo:
        archivo.readline()  # Saltar la primera línea de encabezados
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
            
            
print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")
    
lectura_archivo()
        

productos = []
with open("productos.txt", "r") as archivo:
    archivo.readline()  # Saltar la primera línea de encabezados
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)
    print(f"Lista de productos: {productos}")

###################################################
################ ejercicio 5 ######################
###################################################

def lectura_archivo():
    print("Leyendo con readlines():")
    with open("productos.txt", "r") as archivo:
        archivo.readline()  # Saltar la primera línea de encabezados
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
            
            
print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")
    
lectura_archivo()
        
producto_usuario = input("Ingrese el nombre del producto: ")

with open("productos.txt", "r") as archivo:
    archivo.readline()  # Saltar la primera línea de encabezados
    lineas = archivo.readlines()
    encontrado = False
    for linea in lineas:
        partes = linea.strip().split(",")
        if partes[0].lower() == producto_usuario.lower():
            print(f"Producto encontrado: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
            print("Producto encontrado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("Error: Producto no encontrado.")
        

###################################################
################ ejercicio 6 ######################
###################################################

def lectura_archivo():
    print("Leyendo con readlines():")
    with open("productos.txt", "r") as archivo:
        archivo.readline()  # Saltar la primera línea de encabezados
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
            
            
print("Escribiendo con write()")

with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.write("Frutillas,9000.0,80\n")
    archivo.write("Arandanos,10000.0,25\n")
    archivo.write("Moras,9500.0,100\n")
    
lectura_archivo()
        
producto_usuario = input("Ingrese el nombre del producto: ")

productos = []
with open("productos.txt", "r") as archivo:
    archivo.readline()  # Saltar la primera línea de encabezados
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)
    print(f"Lista de productos: {productos}")
for producto in productos:
    if producto["nombre"].lower() == producto_usuario.lower():
        print(f"Producto encontrado: {producto}")
        break
    else:
        print("Error: Producto no encontrado.")
    
with open("productos.txt", "w") as archivo:
    archivo.write("Producto,Precio,Cantidad\n")
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
