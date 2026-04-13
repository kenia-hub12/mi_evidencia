import time

matriz1 = [
    [10, 22, 33],
    [33, 44, 72],
    [13, 11, 43]
]

matriz2 = [
    [40, 55, 1],
    [22, 41, 91],
    [11, 32, 44]
]

inicio = time.time()

for n in range(100000):
    matrizF = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(len(matrizF)):
        for j in range(3):
            for k in range(3):
                matrizF[i][j] += matriz1[i][k] * matriz2[k][j]

fin = time.time()

for elemento in matrizF:
    print(elemento)

print("Tiempo de ejecución:", fin - inicio, "segundos")