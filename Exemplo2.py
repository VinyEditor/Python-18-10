matriz = []

linhas = int(input("Digite o número de linhas: "))

colunas = int(input("Digite o número de colunas: "))

for i in range(0, linhas, 1) :
    matriz.append([])
    
for l in range(0, linhas, 1):
    for c in range(0, colunas,1):
        num = int(input("Digite um número: "))
        matriz[l].append(num)

print(matriz)

for i in range(0, linhas, 1):
    print(matriz[i])

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        print(matriz[l][c])



