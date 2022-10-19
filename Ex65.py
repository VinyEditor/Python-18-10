#Armazenar seis valores em uma matriz de ordem 2x3. Apresentar os valores na tela

matriz = [ [1,2], [3,4], [5,6] ]

# Mostra a matriz um uma linha única
print(matriz)

# Mostra a matriz de forma real
for i in range(0,3):
    for j in range(0,2):
        print(matriz[i][j], end=" ")
    print()
