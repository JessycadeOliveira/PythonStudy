extenso= ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
          'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
          'Dezoito', 'Dezenove', 'Vinte')
while True:
    num=int(input('Digite um número: '))
    if 0 <= num <=20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {(extenso[num])}')