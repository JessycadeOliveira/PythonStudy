matriz=[[0,0,0], [0,0,0], [0,0,0]]
somapar=somaterceira=maior=0
for l in range(0,3):       #para linha em intervalo de 0 a 2
    for c in range(0,3):     #para coluna no intervalo de 0 a 2
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: ')) #matriz na linha x posicao x recebe o input
print('=-='*30)
for l in range(0,3):    #para linha em intervalo de 0 a 2
    for c in range(0,3):  #para coluna em intervalo de 0 a 2
        print(f'[{matriz[l][c]}]', end='')  #mostra a linha e coluna
        if matriz [l][c]%2==0:          #se o numero em linah coluna for par
            somapar+=matriz[l][c]    #soma par recebe o numero (acumulador)
    print()
print('=-='*30)
print(f'A soma dos valores pares é {somapar}')
for l in range (0,3):     #para linha em intervalo 0 a 2
    somaterceira+=matriz[l][2]    #soma 3 linha recebe ela mesma + a matriz na linha (x) posicao 2 sempre
print(f'A soma dos valores da terceira coluna é {somaterceira}')
for c in range(0,3):   #para coluna em intervalo 0 a 2
    if c==0:           #se for a 1 coluna
        maior=matriz[1][c]  #se for a 1 coluna, o maior recebe o numero da 1 coluna
    elif matriz [1][c]> maior:   #se nao for a 1 coluna, ele verifica se o numero da coluna em questao é >
        maior= matriz [1][c]    #caso seja maior o maior recebe essse numero
print(f'O maior valor da segunda linha é {maior}')
