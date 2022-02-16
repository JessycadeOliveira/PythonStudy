n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
print('CALCULANDO MÉDIA...')
media=(n1+n2)/2
if media < 5.0:
    print(f'Você foi REPROVADO! Sua média foi', {media})
elif media > 5.0 and media < 7.0:
    print(f'Você está de RECUPERAÇÃO! Sua média foi', {media})
else:
    print(f'Parabéns! Você foi aprovado com média de', {media})