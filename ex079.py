lista=[]
while True:
    numero=int(input(f'Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado com sucesso.', end='')
    else:
        print('Número repetido, por favor digite outro número.', end='')
    resposta=str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
