###################################################
################ ejercicio 1 ######################
###################################################
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

def imprimir_factoriales_hasta_n(n):
    if n < 1:
        return
    else:
        imprimir_factoriales_hasta_n(n - 1)
        print(f"Factorial de {n} es {factorial(n)}")
        
#programa principal
numero = int(input("Ingrese un número entero positivo: "))
imprimir_factoriales_hasta_n(numero)


###################################################
################ ejercicio 2 ######################
###################################################
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def imprimir_fibonacci_hasta_n(n):
    if n < 0:
        return
    else:
        imprimir_fibonacci_hasta_n(n - 1)
        print(f"{fibonacci(n)}", end=" ")

numero = int(input("Ingrese un número entero positivo: "))
imprimir_fibonacci_hasta_n(numero)


###################################################
################ ejercicio 3 ######################
###################################################

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
#programa principal
base = int(input("Ingrese la base (número entero): "))
exponente = int(input("Ingrese el exponente (número entero no negativo): "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")

###################################################
################ ejercicio 4 ######################
###################################################

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
#programa principal
numero = int(input("Ingrese un número entero no negativo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")

###################################################
################ ejercicio 5 ######################
###################################################

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] != palabra[-1]:
            return False
        else:
            return es_palindromo(palabra[1:-1])
        
#programa principal
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")   
    
###################################################
################ ejercicio 6 ######################
###################################################

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
#programa principal
numero = int(input("Ingrese un número entero no negativo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")


###################################################
################ ejercicio 7 ######################
###################################################

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
#programa principal
bloques_primer_nivel = int(input("Ingrese la cantidad de bloques del primer nivel: "))
total_bloques = contar_bloques(bloques_primer_nivel)
print(f"La cantidad total de bloques en la pirámide es: {total_bloques}")

###################################################
################ ejercicio 8 ######################
###################################################

def contar_digitos(n, digito):
    if n == 0:
        return 0
    else:
        contador = contar_digitos(n // 10, digito)
        if n % 10 == digito:
            contador += 1
        return contador
    
#programa principal
numero = int(input("Ingrese un número entero no negativo: "))
digito_a_contar = int(input("Ingrese el dígito a contar (0-9): "))
cantidad = contar_digitos(numero, digito_a_contar)
print(f"El dígito {digito_a_contar} aparece {cantidad} veces en el número {numero}.")

