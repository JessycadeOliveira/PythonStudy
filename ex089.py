lista=[]
while True:
    nome=str(input('Nome do aluno: '))
    nota1=float(input('Primeira nota: '))
    nota2=float(input('Segunda nota: '))
    media=(nota1+nota2)/2
    lista.append([nome, [nota1,nota2], media])
    resp=str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-=-'*30)
print(f'{"N":<4}{"Aluno":<10}{"Média":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    escolha=int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if escolha==999:
        print('Finalizando...')
        break
    if escolha<=len(lista)-1:
        print(f'As notas do Aluno {lista[escolha][0]} são {lista[escolha][1]}')
