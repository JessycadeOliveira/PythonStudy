vel=int(input('A quantos kilômetros o seu carro estava?'))
if vel > 80:
    multa = ((vel - 80) * 7)
    print(f'Você foi multado! A sua multa custará R$ {multa} reais')
else:
    print('Parabéns!')
