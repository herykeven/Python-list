##Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma lista;

lista_numeros = []
numeros_negativos = []
numeros_positivos = []

for i in range(4):

    lista_numeros.append(float(input("Digite um número: ")))


for num in lista_numeros:

    if num < 0:
        numeros_negativos.append(num)
    elif num > 0:
        numeros_positivos.append(num)

print(len(numeros_negativos) , "números negativo(s).")

print("A soma total dos números positivos é igual a: " , sum(numeros_positivos))