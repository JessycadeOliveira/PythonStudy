numeros=0
total=[[],[]]
for c in range(1,8):
    numeros=int(input(f'Digite o {c}o. número: '))
    if numeros%2==0:
        total[0].append(numeros)
    else:
        total[1].append(numeros)
print(f'Foram digitados os números ({numeros})')
total[0].sort()
total[1].sort()
print(f'Os números ({total[0]}) são PARES')
print(f'Os números ({total[1]}) são ÍMPARES')
