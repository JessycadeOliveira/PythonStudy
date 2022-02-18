num=int(input('Digite um número para saber seu fatorial: '))
result=1
cont=1
while cont <= num:
    result = result * cont
    cont += 1
print(f'O Fatorial de {num} é igual a {result}')