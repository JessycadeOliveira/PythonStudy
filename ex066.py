soma=quant=0
while True:
    num=int(input('Digite um número: '))
    if num==999:
        break
    quant+=1
    soma+=num
print(f'A soma entre os {quant} números digitados foi {soma}')
