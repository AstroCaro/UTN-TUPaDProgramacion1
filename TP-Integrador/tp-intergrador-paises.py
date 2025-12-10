import csv
import os
import sys
import time

# ============================================================================
# MÓDULO: DATOS
# Gestión de persistencia y manipulación de datos
# ============================================================================11

# Obtener la ruta del directorio donde está este script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(DIRECTORIO_ACTUAL, "paises.csv")

def cargar_paises():
    paises = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo: 
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()
            return paises
        
    with open(NOMBRE_ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": float(fila["superficie"]),
                "continente": fila["continente"]
            }
            paises.append(pais)
    return paises

def persistir_pais(pais):
    with open(NOMBRE_ARCHIVO, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
        escritor.writerow(pais)
        
def persistir_paises(paises):
    with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
            
def agregar_pais_a_lista(paises, nombre, poblacion, superficie, continente):
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    return True

# Opción 1: Agregar país a listado
def agregar_pais(paises):
    datos = solicitar_datos_nuevo_pais(paises)
    if datos is None:
        return
    nombre, poblacion, superficie, continente = datos
    pais_agregado = agregar_pais_a_lista(paises, nombre, poblacion, superficie, continente)
    if pais_agregado:
        persistir_pais({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
        print(f"País '{nombre}' agregado exitosamente.")
        
# Opcion 2: Actualizar los datos de poblacion y superficie de un país en listado
def actualizar_pais(paises):
    nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip()
    if not validar_texto(nombre_buscar):
        print("Error: El nombre del país no es válido.")
        return
    indice = buscar_pais(nombre_buscar, paises)
    if indice == -1:
        print(f"El país '{nombre_buscar}' no se encuentra en el listado.")
        return
    print(f"Actualizando datos para el país '{paises[indice]['nombre']}'")
    nuevos_datos = actualizar_datos(paises)
    if nuevos_datos is None:
        return
    poblacion, superficie = nuevos_datos
    if poblacion is not None:
        paises[indice]['poblacion'] = poblacion
    if superficie is not None:
        paises[indice]['superficie'] = superficie
    persistir_paises(paises)
    print(f"País '{paises[indice]['nombre']}' actualizado exitosamente.")


# ============================================================================
# MÓDULO: VALIDACIONES
# Validación de entradas y solicitud de datos al usuario
# ============================================================================

def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_entero_positivo(valor):
    return valor.isdigit() and int(valor) > 0

def validar_numero_real(valor):
    return valor.isdecimal() and float(valor) > 0

def estandarizar_nombre(nombre):
    return " ".join(nombre).strip().lower().split()

# Solicitud de datos para un nuevo país
def solicitar_nombre_pais(paises):
    nombre_input = input("Ingrese el nombre del país: ").strip()
    if not validar_texto(nombre_input):
        print("Error: El nombre del país no es válido. Intente nuevamente.")
        return solicitar_nombre_pais(paises)
    if nombre_duplicado(nombre_input, paises):
        print("Error: El país ya existe en el listado. Intente nuevamente.")
        return solicitar_nombre_pais(paises)
    return nombre_input

def solicitar_poblacion_pais():
    poblacion_input = input("Ingrese la población del país: ").strip()
    if not validar_entero_positivo(poblacion_input):
        print("Error: La población debe ser un número entero positivo.")
        return solicitar_poblacion_pais()
    return int(poblacion_input)

def solicitar_superficie_pais():
    superficie_input = input("Ingrese la superficie del país (en km²): ").strip()
    if not validar_numero_real(superficie_input):
        print("Error: La superficie debe ser un número positivo.")
        return solicitar_superficie_pais()
    return float(superficie_input)

def solicitar_continente_pais():
    continente_input = input("Ingrese el continente del país: ").strip()
    if not validar_texto(continente_input):
        print("Error: El continente no es válido.")
        return solicitar_continente_pais()
    return continente_input

def solicitar_datos_nuevo_pais(paises):
    nombre = solicitar_nombre_pais(paises)
    poblacion = solicitar_poblacion_pais() 
    superficie = solicitar_superficie_pais()   
    continente = solicitar_continente_pais()
    return nombre, poblacion, superficie, continente
          
def actualizar_datos(paises):
    poblacion_input = input("Ingrese la nueva población del país (deje vacío para no cambiar): ").strip()
    superficie_input = input("Ingrese la nueva superficie del país (deje vacío para no cambiar): ").strip()
    poblacion = None
    superficie = None
    if poblacion_input:
        if not validar_entero_positivo(poblacion_input):
            print("Error: La población debe ser un número entero positivo.")
            return None
        poblacion = int(poblacion_input)
    if superficie_input:
        if not validar_numero_real(superficie_input):
            print("Error: La superficie debe ser un número positivo.")
            return None
        superficie = float(superficie_input)
    return poblacion, superficie


# ============================================================================
# MÓDULO: BÚSQUEDAS
# Funciones para buscar países en el listado
# ============================================================================
def nombre_duplicado(nombre, paises):
    return buscar_pais(nombre, paises) != -1

# Buscar país por nombre y devolver su índice o -1 si no existe 
def buscar_pais(nombre, paises):
    pais_estandarizado = estandarizar_nombre(nombre)
    for i, pais in enumerate(paises):
        if estandarizar_nombre(pais["nombre"]) == pais_estandarizado:
            print(f"País '{nombre}' encontrado en el índice {i}.")
            return i
    return -1

# Opción 3: Buscar un país por nombre
def buscar_pais_por_nombre(paises):
    nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip()
    if not validar_texto(nombre_buscar):
        print("Error: El nombre del país no es válido.")
        return
    indice = buscar_pais(nombre_buscar, paises)
    if indice == -1:
        print(f"El país '{nombre_buscar}' no se encuentra en el listado.")
        return
    pais = paises[indice]
    print(f"País encontrado: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']} km², Continente: {pais['continente']}")
    
    
# ============================================================================
# MÓDULO: FILTROS
# Funciones para filtrar países según diferentes criterios
# ============================================================================

# Opción 4: Filtrar países por continente, rango de población o superficie
def filtrar_paises(paises):
    continente = input("Ingrese el continente para filtrar (o deje vacío para omitir): ").strip()
    poblacion_min = input("Ingrese la población mínima para filtrar (o deje vacío para omitir): ").strip()
    poblacion_max = input("Ingrese la población máxima para filtrar (o deje vacío para omitir): ").strip()
    superficie_min = input("Ingrese la superficie mínima para filtrar (o deje vacío para omitir): ").strip()
    superficie_max = input("Ingrese la superficie máxima para filtrar (o deje vacío para omitir): ").strip()
    resultados = []
    for pais in paises:
        if continente and pais['continente'].lower() != continente.lower():
            continue
        if poblacion_min and pais['poblacion'] < int(poblacion_min):
            continue
        if poblacion_max and pais['poblacion'] > int(poblacion_max):
            continue
        if superficie_min and pais['superficie'] < float(superficie_min):
            continue
        if superficie_max and pais['superficie'] > float(superficie_max):
            continue
        resultados.append(pais)
    for pais in resultados:
        print(f"País: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']} km², Continente: {pais['continente']}")
        

# ============================================================================
# MÓDULO: ORDENAMIENTO
# Funciones para ordenar países según diferentes criterios
# ============================================================================

# Opción 5: Ordenar países por nombre, población o superficie (ascendente o descendente)
def ordenar_paises(paises):
    if not paises:
        print("No hay países en el listado para ordenar.")
        return
    criterio = input("Ingrese el criterio de ordenamiento (nombre/poblacion/superficie): ").strip().lower()
    orden = input("Ingrese el orden (asc/desc): ").strip().lower()
    reverse = orden == "desc"
    paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=reverse)
    for pais in paises_ordenados:
        print(f"País: {pais['nombre']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']} km², Continente: {pais['continente']}")
    

# ============================================================================
# MÓDULO: ESTADÍSTICA
# Funciones para calcular y mostrar estadísticas sobre países
# ============================================================================

# Opción 6: Mostrar estadísticas de los países (pais con mayor y menor población, promedio de población, promedio de superficie, cantidad de países por continente)
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países en el listado para mostrar estadísticas.")
        return
    pais_mayor_poblacion = max(paises, key=lambda x: x['poblacion'])
    pais_menor_poblacion = min(paises, key=lambda x: x['poblacion'])
    promedio_poblacion = sum(p['poblacion'] for p in paises) / len(paises)
    promedio_superficie = sum(p['superficie'] for p in paises) / len(paises)
    paises_por_continente = {}
    for pais in paises:
        continente = pais['continente']
        if continente not in paises_por_continente:
            paises_por_continente[continente] = 0
        paises_por_continente[continente] += 1
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")
    print("Cantidad de países por continente:")
    for continente, cantidad in paises_por_continente.items():
        print(f"  {continente}: {cantidad}")

# ============================================================================
# MÓDULO: BLOQUE MAIN
# Menú principal y flujo del programa
# ============================================================================

def mostrar_menu():
    print("\n" + "="*60)
    print("                     TP INTEGRADOR - PAISES")
    print("="*60)
    print("1. Agregar país a listado")
    print("2. Actualizar país en listado")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("="*60)
    
def barra_progreso(total=20):
    print("\nCargando:", end=" ", flush=True)
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = "█" * i + "-" * (total - i)
        sys.stdout.write(f"\r[{barra}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


def main():
    paises = cargar_paises()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        match opcion: 
            case "1":
                print("★★★★★ AGREGAR PAÍS A LISTADO ★★★★★")
                agregar_pais(paises)
            case "2":
                print("★★★★★ ACTUALIZAR PAÍS EN LISTADO ★★★★★")
                actualizar_pais(paises)
            case "3":
                print("★★★★★ BUSCAR UN PAÍS POR NOMBRE ★★★★★")
                buscar_pais_por_nombre(paises)
            case "4":
                print("★★★★★ FILTRAR PAÍSES ★★★★★")
                filtrar_paises(paises)
            case "5":
                print("★★★★★ ORDENAR PAÍSES ★★★★★")
                ordenar_paises(paises)
            case "6":
                print("★★★★★ MOSTRAR ESTADÍSTICAS ★★★★★")
                mostrar_estadisticas(paises)
            case "7":
                print("Saliendo del programa. ¡Vuelva pronto! 🎉")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        barra_progreso()
        
if __name__ == "__main__":
    main()