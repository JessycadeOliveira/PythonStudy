valor = int(input('Digite o valor que será levantado: '))
if valor >= 50:
    nota50 = valor//50
    valor+= - (50*nota50)
    print(f'Total de {nota50} cédulas de R$50')
if valor >= 20:
    nota20 = valor//20
    valor+= - (20*nota20)
    print(f'Total de {nota20} cédulas de R$20')
if valor >= 10:
    nota10 = valor//10
    valor+= - (10*nota10)
    print(f'Total de {nota10} cédulas de R$10')
if valor >= 1:
    nota1 = valor//1
    valor+= - (1*nota1)
    print(f'Total de {nota1} cédulas de R$1')




