valor=float(input('Qual o valor da casa?R$'))
sal=float(input('Qual o salário do comprador? R$'))
anos=float(input('Em quantos anos pretende pagar?'))
print('Estamos calculando seu empréstimo, aguarde')
prest=(valor/anos)/12
print(f'A prestação da sua casa seria de R$', {prest}, 'mensais')
if prest > (sal * 30/100):
    print('S eu empréstimo foi negado pois o valor da prestação de R$',{prest}, 'excede 30% do seu salário')
else:
    print(f'Parabéns, o seu empréstimo foi aprovado e você pagará', {anos*12}, 'prestações de R$', {prest})