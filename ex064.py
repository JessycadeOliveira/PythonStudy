num=0
cont=0
acum=0
while num!= 999:
    cont+=1
    acum+=num
    num = int(input('Digite um número: '))
print(f'Você digitou {cont-1} números válidos e a soma entre eles é {acum}')
