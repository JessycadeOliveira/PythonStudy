import time
num=int(input('Digite um número: '))
print('VERIFICANDO SE O NÚMERO É PRIMO...')
time.sleep(2)
tot=0
for c in range(1, num+1):
    if num%c==0:
        tot=tot+1
if tot==2:
    print(f'O número {num} É PRIMO')
else:
    print(f'O número {num} NÃO É PRIMO')