soma=0
for n in range(0,6):
    num=int(input('Digite um número inteiro: '))
    if num%2==0:
        soma=soma+n
print(f'A soma entre os valores digitados é {soma}')
