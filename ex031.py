viagem=float(input('Quantos kilômetros terá a sua viagem?'))
if viagem <= 200:
    print('A sua viagem custará R$', viagem*0.5)
else:
    print('A sua viagem custará R$', viagem*0.45)