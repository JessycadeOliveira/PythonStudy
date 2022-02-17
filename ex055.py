maior=0
menor=0
for p in range (1,6):
    peso=float(input(f'Digite o {p} peso: '))
    if p == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print(f'O maior peso lido foi {maior}KG e o menor peso foi {menor}KG')