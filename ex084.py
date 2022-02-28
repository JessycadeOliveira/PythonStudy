geral=[]
pessoas=[]
#cont=0
maior=menor=0 #NOVO
#maior=[]
#menor=[]
#nmaior=[]
#nmenor=[]
while True:
    geral.append(str(input('Nome: ')))      #coloco na lista GERAL na ultima pos o nome
    geral.append(float(input('Peso: ')))    #coloco na lista GERAL na ultima pos o peso, ficando [nome, peso]
    if len(pessoas)==0:   #NOVO
        maior=menor=geral[1] #NOVO
    else:                    #NOVO
        if geral[1]>maior:    #NOVO
            maior=geral[1]    #NOVO
        if geral[1]<menor:    #NOVO
            menor=geral[1]    #NOVO
    pessoas.append(geral[:])         #lista PESSOAS recebe uma copia do conteudo da lista GERAL
    geral.clear()  #NOVO
    #if cont==0:
       # maior.append(geral[:])    #lista MAIOR recebe copia do conteudo da lista geral
       # menor.append(geral[:])    #lista MENOR recebe copia do conteudo da lista geral
    #if maior[0][1]>pessoas[cont][1]:   #se lista MAIOR no index de cont, na pos 1 for > lista PESSOAS
        #maior.append(pessoas[cont])     #no index de cont, na pos 1, MAIOR append PESSOAS na pos cont
        #nmaior.append(pessoas[cont][0])
    #if menor[0][1]<pessoas[cont][1]:    #se lista MENOR no index de cont, na pos 1 for > lista PESSOAS
        #menor.append(pessoas[cont])     #no index de cont, na pos 1, MENOR append PESSOAS na pos cont
        #nmenor.append(pessoas[cont][0])
    resp=str(input('Quer continuar? [S/N]')).upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')  #NOVO len ao inves do cont
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in pessoas:  #NOVO
    if p[1]==maior:   #NOVO
        print(f'({p[0]}) ', end='')  #NOVO
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in pessoas:  #NOVO
    if p[1]==menor:  #NOVO
        print(f'({p[0]}) ', end='')  #NOVO
print()


