from ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 20% temos R${moeda.moeda(moeda.aumentar(p, 20))}')
print(f'Diminuindo 10% temos R${moeda.moeda(moeda.diminuir(p, 10))}')