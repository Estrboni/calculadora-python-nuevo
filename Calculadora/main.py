# Programador1 entrada de datos (Funciones matematicas)
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# Programador2 (Logica principal) junto a Programador3-salida de datos
def iniciar():
    print("\n--- Bienvenido a la MultiCalculadora ---")
    
    # Entrada de datos la de verdad
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    # Programador3 
    # Salida de datos usando f-strings y \n para que se vea bonito y ordenado
    print(f"\n-> Suma: {sumar(num1, num2)}")
    print(f"-> Resta: {restar(num1, num2)}")
    print(f"-> Multiplicacion: {multiplicar(num1, num2)}")
    print(f"-> Division: {dividir(num1, num2)}\n")
    
    # Para que sea infinita sin usar while, la funcion se llama a si misma
    iniciar()

# Llamamos a la funcion para que empiece el bucle otra vez
iniciar()