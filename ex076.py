tupla=('borracha', 1.99, 'lápis', 2.50, 'apontador', 4.20,
       'lapiseira', 1.50, 'caneta', 2.00, 'estojo', 9.90,
       'mochila', 45.90, 'caderno', 5.80 )
print('-='*20)
print(f'{"Listagem de Preços":^36}')
print('-='*20)
for p in range(0,len(tupla)):
    if p%2==0:
        print(f'{tupla[p]:.<30}', end='')
    else:
        print(f'R${tupla[p]:>7.2f}')
print('-='*20)