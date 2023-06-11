import numpy as np


def cuatroporcuatro_matriz():
    # nace
    matriz = np.random.randint(0, 81, (4, 3))
    print("antes")
    print(matriz)
    # se reproduce
    ultima_fila = matriz[-1, :]
    print("---------1")
    print(ultima_fila)
    # se muere
    matriz = np.delete(matriz, -1, axis=0)
    print("---------2")
    print(matriz)
    # consige titulo
    tuned = np.insert(matriz, matriz.shape[1], ultima_fila, axis=1)
    print("---------3")
    print(tuned)
    return tuned
