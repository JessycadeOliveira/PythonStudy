lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A ordem decrescente desses números é: {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
