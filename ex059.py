num1=int(input('Digite o 1º valor: '))
num2=int(input('Digite o 2º valor: '))
print('-=-'*20)
print(f'{num1} -=-=- {num2}')
print('-=-'*20)
print('ESCOLHA UMA DAS OPÇÕES ABAIXO: ')
print('[1] soma dos dois valores')
print('[2] multiplicação os dois valores')
print('[3] maior entre os dois valores')
print('[4] escolha novos valores')
print('[5] sair do programa')
resp=int(input('.: '))
while resp!=5:
    if resp==1:
        soma=num1+num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}')
        print('-=-' * 10)
        resp=int(input('Escolha uma nova opção: '))
    if resp==2:
        mult=num1*num2
        print(f'A multiplicação entre {num1} e {num2} é igual a {mult}')
        print('-=-' * 10)
        resp = int(input('Escolha uma nova opção: '))
    if resp==3:
        if num1>num2:
            print(f'O número {num1} é maior do que o número {num2}')
        elif num1<num2:
            print(f'O número {num2} é maior do que o número {num1}')
        else:
            print(f'O número {num1} e o número {num2} são iguais!')
        print('-=-' * 10)
        resp = int(input('Escolha uma nova opção: '))
    if resp==4:
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digite o 2º valor: '))
        print('-=-' * 20)
        print(f'{num1} -=-=- {num2}')
        print('-=-' * 20)
        print('ESCOLHA UMA DAS OPÇÕES ABAIXO: ')
        print('[1] soma dos dois valores')
        print('[2] multiplicação os dois valores')
        print('[3] maior entre os dois valores')
        print('[4] escolha novos valores')
        print('[5] sair do programa')
        resp = int(input('.: '))

    validas = [1, 2, 3, 4, 5]
    if resp not in validas:
        resp = int(input('Opção inválida, escolha novamente: '))
print('PROGRAMA ENCERRADO PELO USUÁRIO')


