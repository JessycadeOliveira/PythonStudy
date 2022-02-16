import random
print('-=-'*20)
print('Vamos jogar Jokenpo?')
print('-=-'*20)
lista=['Pedra', 'Papel', 'Tesoura']
pc=str(random.choice(lista))
jogador=str(input('Você escolhe Pedra, Papel ou Tesoura?')).strip()
jogador=jogador.lower()
print(f'CPU {pc}  VS  {jogador} Jogador')
if pc== 'Pedra' and jogador == 'pedra':
    print('Eu escolhi pedra e você também, foi empate!')
elif pc== 'Pedra' and jogador == 'tesoura':
    print('EU GANHEI! Pedra esmaga a Tesoura')
elif pc=='Pedra' and jogador == 'papel':
    print('VOCÊ GANHOU! Papel envolve a Pedra')
elif pc== 'Papel' and jogador == 'papel':
    print('Eu escolhi papel e você também, foi empate!')
elif pc== 'Papel' and jogador =='pedra':
    print('EU GANHEI! Papel envolve a Pedra')
elif pc== 'Papel' and jogador =='tesoura':
    print('VOCÊ GANHOU! A tesoura corta o Papel')
elif pc== 'Tesoura' and jogador == 'tesoura':
    print('Eu escolhi tesoura e você também, foi empate!')
elif pc== 'Tesoura' and jogador== 'pedra':
    print('VOCÊ GANHOU! A pedra esmaga a Tesoura')
elif pc== 'Tesoura' and jogador == 'papel':
    print('EU GANHEI! Tesoura corta o Papel')
