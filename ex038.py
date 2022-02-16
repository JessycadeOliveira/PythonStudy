n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
if n1>n2:
    print(f'O primeiro número,', {n1}, 'é maior do que o segundo número,', {n2})
elif n1==n2:
    print(f'Os dois números são iguais!')
else:
    print(f'O segundo número,', {n2}, 'é maior do que o primeiro número,', {n1})