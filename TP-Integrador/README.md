# 📘 Trabajo Práctico Integrador – Programación I
## Gestión de Datos de Países en Python

---

## 🏫 Datos Institucionales

**Universidad:** Universidad Tecnológica Nacional (UTN)  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia (TUPaD)  
**Materia:** Programación I  
**Año Académico:** 2025  

---

## 👩‍💻 Integrante

**Carolina Silva**  
Año académico 2025

---

## 📌 Descripción del Proyecto

Este Trabajo Práctico Integrador consiste en el desarrollo de una **aplicación en Python** capaz de gestionar información sobre países, aplicando conceptos fundamentales de la materia **Programación I**.

### ✨ Funcionalidades principales:

✅ **Cargar países** con sus datos principales (nombre, población, superficie, continente)  
✅ **Actualizar registros** existentes (modificar población y superficie)  
✅ **Buscar países** por nombre con coincidencia exacta o parcial  
✅ **Filtrar** por múltiples criterios (continente, rangos de población y superficie)  
✅ **Ordenar** la información de forma dinámica (ascendente/descendente)  
✅ **Obtener estadísticas** generales (promedios, máximos, mínimos, agrupaciones)  
✅ **Persistir datos** en archivo CSV para mantener información entre sesiones  

### 🎯 Conceptos aplicados:

El proyecto integra los siguientes temas de la materia:

- **Estructuras de datos:** listas, diccionarios
- **Funciones:** modularización y reutilización de código
- **Validaciones:** control de entradas del usuario
- **Estructuras de control:** bucles (`for`, `while`), condicionales (`if`, `match`)
- **Algoritmos de ordenamiento:** uso de `sorted()` con criterios personalizados
- **Estadísticas:** cálculos agregados (suma, promedio, máximo, mínimo)
- **Manejo de archivos:** lectura y escritura en formato CSV
- **Organización modular:** separación lógica por responsabilidades

---

## 🧱 Estructura del Proyecto

```
📦 TP-Integrador-Paises
 ├── tp-integrador-paises.py              # Programa principal con código modularizado
 ├── paises.csv           # Archivo de persistencia de datos (se genera automáticamente)
 └── README.md            # Documentación del proyecto
```

### 📋 Módulos Internos

El programa está organizado en **7 módulos lógicos** dentro del archivo `main.py`:

| Módulo | Responsabilidad | Funciones principales |
|--------|----------------|----------------------|
| **Datos** | Gestión de persistencia y operaciones CRUD | `cargar_paises()`, `persistir_pais()`, `persistir_paises()`, `agregar_pais()`, `actualizar_pais()` |
| **Validaciones** | Control de entradas y solicitud de datos | `validar_texto()`, `validar_entero_positivo()`, `validar_numero_real()`, `estandarizar_nombre()`, funciones `solicitar_*()` |
| **Búsquedas** | Localización de países | `buscar_pais()`, `nombre_duplicado()`, `buscar_pais_por_nombre()` |
| **Filtros** | Selección condicional de países | `filtrar_paises()` |
| **Ordenamiento** | Organización de listado | `ordenar_paises()` |
| **Estadística** | Cálculos agregados | `mostrar_estadisticas()` |
| **Main** | Flujo principal y menú | `main()`, `mostrar_menu()`, `barra_progreso()` |

---

## ▶️ Instrucciones de Ejecución

### 📋 Requisitos Previos

- **Python 3.10 o superior** instalado en el sistema
- **No requiere librerías externas** (solo módulos estándar de Python)

### 🚀 Pasos para Ejecutar

1. **Clonar el repositorio:**

```bash
git clone https://github.com/AstroCaro/UTN-TUPaDProgramacion1.git
```

2. **Ingresar a la carpeta del TP:**

```bash
cd UTN-TUPaDProgramacion1/TP-Integrador
```

3. **Ejecutar el programa:**

```bash
python tp-integrador-paises.py
```

4. **Interactuar con el menú:**

Al ejecutar, se mostrará el menú interactivo:

```
============================================================
                     TP INTEGRADOR - PAISES
============================================================
1. Agregar país a listado
2. Actualizar país en listado
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir
============================================================
```

---

## 📚 Librerías Utilizadas

El proyecto utiliza **únicamente librerías estándar de Python**, sin dependencias de terceros:

| Librería | Propósito |
|----------|-----------|
| `csv` | Lectura y escritura del archivo de datos |
| `os` | Manejo de rutas y verificación de existencia de archivos |
| `sys` | Salida estándar para barra de progreso |
| `time` | Animación de barra de carga |

✅ **No requiere instalación adicional** de paquetes externos.

---

## 🧪 Ejemplos de entras y salidas

### ✔ 1. Agregar un País

**Entrada:**
```
Ingrese el nombre del país: Argentina
Ingrese la población del país: 46000000
Ingrese la superficie del país (en km²): 2780000
Ingrese el continente del país: América
```

**Salida:**
```
País 'Argentina' agregado exitosamente.
```

---

### ✔ 2. Búsqueda Parcial

**Entrada:**
```
Ingrese el nombre del país a buscar: arg
```

**Salida:**
```
País: Argentina, Población: 46000000, Superficie: 2780000.0 km², Continente: América
```

---

### ✔ 3. Actualizar País

**Entrada:**
```
Ingrese el nombre del país a actualizar: Argentina
Ingrese la nueva población del país (deje vacío para no cambiar): 47000000
Ingrese la nueva superficie del país (deje vacío para no cambiar): 
```

**Salida:**
```
País 'Argentina' encontrado en el índice 0.
Actualizando datos para el país 'Argentina'
País 'Argentina' actualizado exitosamente.
```

---

### ✔ 4. Filtrar Países

**Entrada:**
```
Ingrese el continente para filtrar (o deje vacío para omitir): América
Ingrese la población mínima para filtrar (o deje vacío para omitir): 40000000
Ingrese la población máxima para filtrar (o deje vacío para omitir): 
Ingrese la superficie mínima para filtrar (o deje vacío para omitir): 
Ingrese la superficie máxima para filtrar (o deje vacío para omitir): 
```

**Salida:**
```
País: Argentina, Población: 46000000, Superficie: 2780000.0 km², Continente: América
País: Estados Unidos, Población: 331000000, Superficie: 9833520.0 km², Continente: América
```

---

### ✔ 5. Ordenamiento

**Entrada:**
```
Ingrese el criterio de ordenamiento (nombre/poblacion/superficie): poblacion
Ingrese el orden (asc/desc): desc
```

**Salida:**
```
País: China, Población: 1400000000, Superficie: 9596961.0 km², Continente: Asia
País: India, Población: 1380000000, Superficie: 3287263.0 km², Continente: Asia
País: Estados Unidos, Población: 331000000, Superficie: 9833520.0 km², Continente: América
```

---

### ✔ 6. Estadísticas

**Salida:**
```
País con mayor población: China (1400000000)
País con menor población: Islandia (370000)
Promedio de población: 328123500.00
Promedio de superficie: 5443151.50 km²
Cantidad de países por continente:
  Asia: 3
  América: 2
  Europa: 1
```

---

## 📂 Formato del Archivo CSV

El archivo `paises.csv` tiene la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,46000000,2780000.0,América
Brasil,213000000,8515767.0,América
China,1400000000,9596961.0,Asia
```

**Campos:**
- `nombre`: Texto (nombre del país)
- `poblacion`: Entero (cantidad de habitantes)
- `superficie`: Decimal (área en km²)
- `continente`: Texto (continente al que pertenece)

---

## 🎥 Video Explicativo

👉 **Video del Trabajo Práctico:** [Video](https://youtu.be/6fsPilScWLw)

---

## 🔗 Repositorio Oficial

👉 **GitHub:** [https://github.com/AstroCaro/UTN-TUPaDProgramacion1/tree/main/TP-Integrador](https://github.com/AstroCaro/UTN-TUPaDProgramacion1/tree/main/TP-Integrador)

---

## 🎉 Créditos

**Proyecto desarrollado por Carolina Silva**  
Tecnicatura Universitaria en Programación a Distancia – UTN  
Materia: Programación I — Año 2025

---

## 📜 Licencia

Este proyecto es de carácter académico y fue desarrollado como parte de la cursada de **Programación I** en la **UTN**.

---

**¿Preguntas o sugerencias?** Podés contactarme a través de mi correo silvagarcesc@gmail.com.

---

*Última actualización: Diciembre 2024*