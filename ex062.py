print('GERADOR DE PA')
print('-='*10)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
cont=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while cont <=total:
        print(f'{termo}->', end='')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais=int(input('Quantos termos a mais você quer mostrar?'))
print(f'A progressão foi encerrada e mostrou {total} termos')
