import random
print('Pensei num número, vc consegue descobrir qual é?')
lista= [0,1,2,3,4,5]
n=int(random.choice(lista))
n2=int(input('Digite o seu palpite:'))
if n == n2:
    print('Parabéns, o número era mesmo', n)
else:
    print('Você errou! o número era:', n)
