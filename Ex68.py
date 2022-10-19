#Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. Após a digitação dos valores solicitar uma constante multiplicativa, que deverá multiplicar cada valor matriz e armazenar o resultado na própria matriz, nas posições correspondentes.

matriz = [[0 for x in range(4)] for x in range(3)]
for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input("Digite um valor: "))
constante = int(input("Digite uma constante: "))
for i in range(3):
    for j in range(4):
        matriz[i][j] = matriz[i][j] * constante
for i in range(3):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()

