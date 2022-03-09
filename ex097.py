def escreva(mensagem):
    tamanho=len(mensagem)+4
    print('~'*tamanho)
    print(f'  {mensagem}')
    print('~'*tamanho)


mensagem=str(input('Digite sua mensagem: '))
escreva(mensagem)

