from time import sleep
def maior(*num):
    cont=maior=0
    print('=-='*20)
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        cont+=1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')


maior(8, 2, 7, 99, 1)
maior(1, 2, 3)
maior(-1, 0, 5)