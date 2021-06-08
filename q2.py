###Faça um programa que lê o sexo de 3 pessoas em uma lista, calcula e exibe a quantidade de pessoas de cada sexo
lista = []
man = []
women = []

for i in range(3):
    lista.append(input("Digite seu sexo com F ou M: ").upper())

for men in lista:
    if men == 'M':
        men = 'M'
        man.append(men)
    else:
        men == 'F'
        men = 'F'
        women.append(men)
print(len(man) , "Masculino(s)")
print(len(women) , "Feminino(s)")
