###
opiniao = []
bom = []
regular = []
otimo = []
for i in range(5):
    opiniao.append(input("\nótimo – 3 \nbom – 2 \nregular – 1.\nDigite sua opinião sobre o filme: ").upper())

for a in opiniao:
    if a == '2':
        a = '2'
        bom.append(a)
    elif a == '1':
        a = '1'
        regular.append(a)
    elif a == '3':
        a = '3'
        otimo.append(a)
print(len(bom) , " Pessoas votaram em 'bom'. ")
print(len(regular) , "Pessoas votaram em 'regular'")
print(len(otimo) , "Pessoas votaram em 'otimo'")

