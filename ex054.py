maior=0
menor=0
for n in range(0,6):
    idade=int(input('Digite sua idade: '))
    if idade >= 21:
        maior=maior+1
    else:
        menor=menor+1
print(f'Neste grupo de 7 pessoas, temos {maior} pessoas maiores de 21 e {menor} pessoas menores de 21 anos')