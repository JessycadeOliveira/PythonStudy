num=int(input('Digite um número de elementos que deseja ver:'))
cont=0
anterior=0
atual=1
print(anterior, '> ', end = '')
print(atual, '> ', end = '')
while cont<num:
    banco=atual
    atual+=anterior
    anterior=banco
    cont+=1
    print(atual, '> ', end = '')
