idade=int(input('Qual a sua idade?'))
if idade < 18:
    print(f'Dentro de', {18-idade}, 'anos você terá que se alistar')
elif idade==18:
    print('Você tem 18 anos e chegou a hora de se alistar!')
else:
    print(f'Você tem', {idade}, 'anos e deveria ter se alistado há', {idade-18}, 'anos atrás')