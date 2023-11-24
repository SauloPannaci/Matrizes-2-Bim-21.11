###### EXERCICIO ######
# Adicione elementos de forma aleatória em uma matriz n X me retorne a quantidade de 
# numeros pares!#

import random
def criar_matriz(n, m):
    matriz = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]
    return matriz
def contar_pares(matriz):
    quantidade_pares = sum(elemento % 2 == 0 for linha in matriz for elemento in linha)
    return quantidade_pares
n = 3  
m = 4 
matriz_aleatoria = criar_matriz(n, m)
print("Matriz Aleatória:")
for linha in matriz_aleatoria:
    print(linha)
quantidade_pares = contar_pares(matriz_aleatoria)
print(f"Quantidade de Números Pares na Matriz: {quantidade_pares}")




