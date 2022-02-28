import random
lista=[] #lista temporaria
jogos=[]  #lista composta por todos os jogos
quant=int(input('Quantos jogos você quer gerar?'))
tot=1
while tot<= quant:  #enquanto total for menor do que a quant q a pessoa escolheu o loop vai rodar
    cont=0
    while True:   #loop infinito
        num=random.randint(1,60) #sorteia um num randomico entre 1 e 60
        if num not in lista:   #se o num n estiver na lista
            lista.append(num)   #adiciona o num na lista
            cont+=1
        if cont >=6:   #se contador maior ou iual a 6
            break     #quebra o loop  e volta pro while da linha 6
    lista.sort()     #ordeno a lista
    jogos.append(lista[:])   #lista jogos recebe uma copia da lista temporaria
    lista.clear()            #limpo a lista temporaria p no prox loop ela guardar so o jogo daquele loop
    tot+=1
print(f'Sorteando {quant} jogos')
for i, l in enumerate(jogos):   #para cada indice (i) na lista (l) em jogos:
    print(f'Jogo {i+1}:{l}')   #mostro o jogo no indice+1 (pq o 1 indice eh 0): o conteudo da lista (6 num)