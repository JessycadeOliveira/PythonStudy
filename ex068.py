import random
cont=0
computador=random.randint(0,10)
print('Vamos jogar par ou ímpar!')
while True:
    jogador=int(input('Seu número: '))
    palpite=str(input('Par ou ímpar: ')).strip().upper()
    soma=jogador+computador
    if soma %2==0:
        vencedor='PAR'
    if soma %2==1:
        vencedor='IMPAR'
    if palpite==vencedor:
        cont+=1
        print('Você ganhou!')
    if palpite!=vencedor:
        break
print(f'Escolhi {computador} e você {jogador}, que somados são {soma}, portanto é um número {vencedor}')
print(f'Você PERDEU depois de ganhar {cont} vezes')


