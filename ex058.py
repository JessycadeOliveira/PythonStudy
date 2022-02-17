import random
tot=0
print('Pensei em um número de 0 a 10, você consegue descobrir qual foi?')
num=int(random.randint(0,10))
num2=int(input('Digite o seu palpite: '))
while num!=num2:
    print(f'Você errou!')
    num2 = int(input('Digite o seu outro palpite: '))
    tot+=1
print(f'Parabéns, você escolheu o número {num2} e eu pensei no número {num}, e você acertou depois de {tot} vezes')
