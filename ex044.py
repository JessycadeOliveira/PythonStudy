import time
valor=float(input('Digite o valor da compra: R$'))
time.sleep(1)
print('Escolha a opção de pagamento abaixo:')
time.sleep(1)
print('-=-'*20)
time.sleep(1)
print('1 - A vista no dinheiro/cheque')
time.sleep(1)
print('2 - A vista no cartão')
time.sleep(1)
print('3 - Em 2x no cartão')
time.sleep(1)
print('4 - Em 3x ou mais no cartão')
time.sleep(1)
print('-=-'*20)
time.sleep(1)
escolha=int(input('Digite a opção desejada:'))
if escolha == 1:
    print(f'A sua compra teve 10 por cento de desconto e ficará por R${valor-(valor*10/100)}')
elif escolha == 2:
    print(f'A sua compra teve 5 por cento de desconto e ficará por R${valor-(valor*5/100)}')
elif escolha == 3:
    print(f'A sua compra não teve nenhum desconto e ficará por R$ {valor}')
elif escolha ==4:
    print(f'A sua compra terá um acréscimo de 20 por cento de juros, passando a custar R$ {valor+(valor*20/100)}')
else:
    print('Você se enganou ao digitar, comece novamente')