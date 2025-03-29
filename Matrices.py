import numpy as np

def pedir_dimensiones():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    return filas, columnas

def pedir_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

def sumar_matrices(A, B):
    if A.shape == B.shape:
        return A + B
    else:
        return "No se pueden sumar matrices de diferentes dimensiones."

def multiplicar_escalar(matriz, escalar):
    return escalar * matriz

def multiplicar_matrices(A, B):
    if A.shape[1] == B.shape[0]:
        return np.dot(A, B)
    else:
        return "No se pueden multiplicar matrices con estas dimensiones."

def determinante(matriz):
    if matriz.shape[0] == matriz.shape[1]:
        return np.linalg.det(matriz)
    else:
        return "No se puede calcular el determinante de una matriz no cuadrada."

def inversa(matriz):
    if matriz.shape[0] == matriz.shape[1]:
        try:
            return np.linalg.inv(matriz)
        except np.linalg.LinAlgError:
            return "La matriz no tiene inversa."
    else:
        return "No se puede calcular la inversa de una matriz no cuadrada."

def resolver_sistema(A, B):
    if A.shape[0] == A.shape[1] and A.shape[0] == B.shape[0]:
        try:
            return np.linalg.solve(A, B)
        except np.linalg.LinAlgError:
            return "El sistema no tiene solución única."
    else:
        return "Las dimensiones de las matrices no son adecuadas para resolver el sistema."

# Programa principal
print("Programa de operaciones con matrices")
filas, columnas = pedir_dimensiones()
A = pedir_matriz(filas, columnas)
B = pedir_matriz(filas, columnas)

print("Suma de matrices:")
print(sumar_matrices(A, B))

escalar = float(input("Ingrese un escalar para multiplicar la primera matriz: "))
print("Multiplicación por escalar:")
print(multiplicar_escalar(A, escalar))

filas_b, columnas_b = pedir_dimensiones()
B = pedir_matriz(filas_b, columnas_b)

print("Multiplicación de matrices:")
print(multiplicar_matrices(A, B))

print("Determinante de la primera matriz:")
print(determinante(A))

print("Inversa de la primera matriz:")
print(inversa(A))

print("Resolviendo sistema de ecuaciones AX = B:")
solucion = resolver_sistema(A, B)
print(solucion)
