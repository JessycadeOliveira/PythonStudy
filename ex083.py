expressao=str(input('Digite a sua expressão: '))
pardeparenteses=[]
for simbolo in expressao:
    if simbolo=='(':
        pardeparenteses.append('(')
    elif simbolo==')':
        if len(pardeparenteses)>0:
            pardeparenteses.pop()
        else:
            pardeparenteses.append(')')
            break
if len(pardeparenteses) ==0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')