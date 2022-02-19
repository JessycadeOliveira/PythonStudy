soma=cont=0
while True:
    cont+=1
    n=int(input('Digite um número:'))
    if n<0:
        break
    for cont in range(1,11):
        print(f'{n} x {cont}= {n*cont}')
print('Fim do programa Tabuada')