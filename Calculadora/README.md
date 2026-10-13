# 🧮 MultiCalculadora en Python

## Descripción
Este proyecto es una calculadora básica desarrollada en Python que permite realizar y mostrar de forma simultánea las operaciones matemáticas fundamentales (suma, resta, multiplicación y división) para dos números ingresados por el usuario, utilizando un enfoque recursivo para la ejecución continua del programa.

## Características
- Operaciones aritméticas básicas: suma, resta, multiplicación y división.
- Ejecución simultánea de todas las operaciones para cada par de números ingresados.
- Interfaz por consola limpia y estructurada utilizando `f-strings` y saltos de línea (`\n`).
- Bucle de ejecución continua implementado mediante **recursividad** (sin emplear bucles `while`).

## Requisitos
- Python 3.6 o superior

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Estrboni/Calculadora-Python.git
   ```

---

## 🔢 Funciones Matemáticas (Programador 1)

En esta fase se implementaron las funciones aritméticas básicas de forma independiente, aplicando el principio de responsabilidad única.

### 🛠️ Componentes Principales:
- **`sumar(a, b)`**: Retorna la suma de los dos operandos.
- **`restar(a, b)`**: Retorna la resta de los dos operandos.
- **`multiplicar(a, b)`**: Retorna la multiplicación de los dos operandos.
- **`dividir(a, b)`**: Retorna la división de los dos operandos.

### 💻 Ejemplo de Implementación:
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b
```

---

## 💻 Lógica Principal y Salida de Datos (Programadores 2 y 3)

En esta fase se integró la interacción con el usuario, la captura de datos y la visualización de resultados mediante `f-strings`, incorporando además un mecanismo de llamada recursiva para mantener el programa en ejecución continua.

### 🛠️ Componentes Principales:
- **`iniciar()`**: Función centralizadora que solicita los valores numéricos, procesa las operaciones simultáneamente, imprime el reporte estructurado y se autoinvoca para reiniciar el ciclo de ejecución.

### 💻 Ejemplo de Implementación:
```python
def iniciar():
    print("\n--- Bienvenido a la MultiCalculadora ---")
    
    # Entrada de datos
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    # Salida de datos usando f-strings y \n
    print(f"\n-> Suma: {sumar(num1, num2)}")
    print(f"-> Resta: {restar(num1, num2)}")
    print(f"-> Multiplicacion: {multiplicar(num1, num2)}")
    print(f"-> Division: {dividir(num1, num2)}\n")
    
    # Bucle infinito mediante recursividad
    iniciar()

# Llamada inicial para arrancar el programa
iniciar()
```