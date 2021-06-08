##Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:

lista_produtos = []
lista50= []
lista_50_80 = []
lista80 = []
for i in range(5):

    lista_produtos.append(float(input("Digite o preço do produto: ")))

for num in lista_produtos:

    if num < 50:
        lista50.append(num)
    elif num >= 50 and num <=80:
        lista_50_80.append(num)
    elif num > 80:
        lista80.append(num)

media = sum(lista_produtos) / 5
#A quantidade de produtos com preço inferior a R$ 50,00;
print(len(lista50) , "produtos abaixo de 50.00R$")
#A quantidade de produtos com preço entre R$ 50,00 e 80,00;
print(len(lista_50_80) , "produtos entre 50.00R$ e 80.00R$")
#A quantidade de produtos com preço acima de R$ 80,00
print(len(lista80) , "produtos acima de 80.00R$")
#A média de preço dos produtos;
print("Média dos produtos:" , media)