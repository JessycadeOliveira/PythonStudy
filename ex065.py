resp= 'S'
cont=0
acum=0
while resp == 'S':
    num=int(input('Digite um número: '))
    if cont==0:
        maior=num
        menor=num
    if num>maior:
        maior=num
    if num<menor:
        menor=num
    cont+=1
    acum+=num
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    while resp not in 'SN':
        resp=str(input('Resposta Inválida. Deseja continuar? [S/N]')).strip().upper()
print(f'Você digitou {cont} valores e a média entre eles é {acum/cont}')
print(f'O maior número digitado foi {maior} e o menor número foi {menor}')
