idade=int(input('Digite a sua idade:'))
if idade < 9:
    print(f'Você tem', {idade}, 'anos e será da categoria MIRIM')
elif idade >= 9 and idade < 14:
    print(f'Você tem', {idade}, 'anos e será da categoria INFANTIL')
elif idade >= 14 and idade < 19:
    print(f'Você tem', {idade}, 'anos e será da categoria JUNIOR')
elif idade >= 19 and  idade < 25:
    print(f'Você tem', {idade}, 'anos e será da categoria SENIOR')
else:
    print(f'Você tem', {idade}, 'anos e será da categoria MASTER')