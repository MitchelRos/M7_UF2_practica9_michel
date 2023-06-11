import numpy as np


def mk_matriz():
    filas = int(input("Ingresa el número de filas pls: "))
    columnas = int(input("Ingresa el número de columnas pls: "))
    matriz = np.random.randint(0, 101, (filas, columnas))
    return matriz


def matriz(matriz):
    print("Matriz:")
    print(matriz)


def redimensionar(matriz, filas, columnas):
    digimon = matriz.reshape(filas, columnas)
    return digimon


def mostrar(redimensionar):
    print("Matriz redimensionada!!!:")
    print(redimensionar)


def valor_maximo(matriz):
    return np.max(matriz)


def valor_minimo(matriz):
    return np.min(matriz)
