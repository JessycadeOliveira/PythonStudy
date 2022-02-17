media=0
maioridade=0
mulmenvin=0
for p in range (1,5):
    nome=str(input('Digite seu nome: '))
    idade=int(input('Digite sua idade: '))
    media+=idade
    sexo=str(input('Digite seu sexo: [F/M] ')).strip().upper()
    if idade>maioridade and sexo=='M':
        maioridade=idade
        nomemaisvelho=nome
    if sexo=='F' and idade<20:
        mulmenvin+=1
        if mulmenvin==1:
            mulher='mulher'
        else:
            mulher='mulheres'
media=media/p
print(f'A média de idade do grupo foi de {media} anos')
print(f'O homem mais velho foi {nomemaisvelho}, que tem {maioridade} anos')
print(f'O total de mulheres com menos de 20 anos foi de {mulmenvin} {mulher}')