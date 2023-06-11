import numpy as np
import Exercici2
import Exercici3
import Exercici4

# Ejercicio 1
print("Ejercicio 1:")
matriz = np.load('exercici1.npy')
print("Matriz:")
print(matriz)
print("Dimensión de la matriz:", matriz.shape)
print("Tamaño de la matriz:", matriz.size)
print("Número total de elementos:", matriz.size)
print("Tipo de elementos internos:", matriz.dtype)

# Ejercicio 2
print("Ejercicio 2:")
print("Matriz 1:")
print(Exercici2.array1())
print("Matriz 2:")
print(Exercici2.array2())
print("Matriz 3:")
print(Exercici2.array3())
print("Número total de elementos:", Exercici2.array1().size + Exercici2.array2().size + Exercici2.array3().size)
print("Dimensión de la matriz 1:", Exercici2.array1().shape)
print("Dimensión de la matriz 2:", Exercici2.array2().shape)
print("Dimensión de la matriz 3:", Exercici2.array3().shape)
print("Tipo de elementos internos:", Exercici2.array1().dtype)
print("Tamaño de la matriz 1:", Exercici2.array1().size)
print("Tamaño de la matriz 2:", Exercici2.array2().size)
print("Tamaño de la matriz 3:", Exercici2.array3().size)

# Ejercicio 3
print("Ejercicio 3:")
# la matriz tiene que ser de 2 y 6 por desgracia para no poner inputs en dos lados
matriz_generada = Exercici3.mk_matriz()
Exercici3.matriz(matriz_generada)
remadiochino = Exercici3.redimensionar(matriz_generada, 2, 6)
Exercici3.mostrar(remadiochino)
valor_maximo = Exercici3.valor_maximo(matriz_generada)
valor_minimo = Exercici3.valor_minimo(matriz_generada)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)

# Ejercicio 4
print("Ejercicio 4:")
TUNEO = Exercici4.cuatroporcuatro_matriz()
print("despues")
print(TUNEO)
