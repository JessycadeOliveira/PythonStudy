peso=float(input('Digite o seu peso:'))
alt=float(input('Digite sua altura:'))
imc= peso/(alt**2)
if imc < 18.5:
    print(f'Seu imc é de {imc} e você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é de {imc} e você está no PESO IDEAL')
elif imc>=25 and imc < 35:
    print(f'Seu imc é de {imc} e você está no SOBREPESO')
elif imc >= 35 and imc < 40:
    print(f' O seu imc é de {imc} e você está com OBESIDADE')
else:
    print(f' O seu imc é de {imc} e você está com OBESIDADE MÓRBIDA')

