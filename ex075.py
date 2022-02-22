tupla=(int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores: {tupla}')
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro número 3 digitado foi na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n %2==0:
        print(n, end=' ')
