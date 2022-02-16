r1=int(input('Digite o comprimento da primeira reta:'))
r2=int(input('Digite o conmprimento da segunda reta:'))
r3=int(input('Digite o comprimento da terceira reta:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('As retas acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('As retas acima NÃO PODEM formar um triângulo!')