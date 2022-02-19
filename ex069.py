homem=maior=mulher=0
while True:
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo =='M':
        homem+=1
    if idade > 18:
        maior+=1
    if sexo=='F' and idade<20:
        mulher+=1
    resp=str(input('Quer cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Das pessoas cadastradas, {maior} são maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulher} mulheres menores de 20 anos')

