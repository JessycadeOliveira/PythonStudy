geral=[]
pessoas=[]
maior=menor=0
while True:
    geral.append(str(input('Nome: ')))
    geral.append(float(input('Peso: ')))
    if len(pessoas)==0:   #NOVO
        maior=menor=geral[1]
    else:
        if geral[1]>maior:
            maior=geral[1]
        if geral[1]<menor:
            menor=geral[1]
    pessoas.append(geral[:])
    geral.clear()
    resp=str(input('Quer continuar? [S/N]')).upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in pessoas:
    if p[1]==maior:
        print(f'({p[0]}) ', end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in pessoas:
    if p[1]==menor:
        print(f'({p[0]}) ', end='')
print()


