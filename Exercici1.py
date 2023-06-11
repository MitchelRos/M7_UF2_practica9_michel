import numpy as np


def crear_matriz():
    matriz = np.diag(np.arange(50))
    np.save('exercici1.npy', matriz)


crear_matriz()
