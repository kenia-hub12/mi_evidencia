matriz1 = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

matrizF = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(len(matrizF)):
    for j in range(4):
        for k in range(3):
            matrizF[i][j] = matrizF[i][j] + matriz1[i][k] * matriz2[k][j]

for elemento in matrizF:
    print(elemento)