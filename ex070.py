total=maior=menor=quant=0
while True:
    nome=str(input('Nome de produto: ')).strip()
    preço=float(input('Preço do produto: R$ '))
    total+=preço
    quant+=1
    if menor==0:
        menor=preço
        barato=nome
    if preço > 1000:
        maior+=1
    if preço < menor:
        menor=preço
        barato=nome
    resp=str(input('Deseja adicionar mais um item? [S/N] ')).strip()
    if resp in 'Nn':
        break
print(f'Você comprou {quant} itens e a sua compra foi de R${total}.')
print(f'Você comprou {maior} produtos que custam mais de R$1000,00')
print(f'O produto mais barato da sua compra foi {barato}, que custou R$ {menor}')



