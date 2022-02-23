lista=[]
par=[]
impar=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for indice, valor in enumerate(lista):
    if valor%2==0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Sua lista completa é {lista}')
print(f'Sua lista somente com números pares é {par}')
print(f'Sua lista somente com números ímpares é {impar}')
