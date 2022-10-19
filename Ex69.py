#Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. Após a digitação dos valores solicitar uma constante multiplicativa, que deverá multiplicar cada valor matriz e armazenar o resultado em outra matriz de mesma ordem, nas posições correspondentes. Exibir as matrizes na tela, sob a forma matricial, ou seja, linhas por colunas.

matriz = []
matriz2 = []

for i in range(3):
    linha = []
    for j in range(4):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)
print(matriz)

constante = int(input("Digite uma constante: "))
for i in range(3):
    linha = []
    for j in range(4):
        linha.append(matriz[i][j] * constante)
    matriz2.append(linha)
print(matriz2)

