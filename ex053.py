frase=str(input('Digite uma frase: ')).strip().upper().split()
frase=''.join(frase)
frase2=''
for c in range(len(frase)-1, -1 , -1):
    frase2+=frase[c]
if frase==frase2:
    print(f'A frase: "{frase}" ao contrário fica "{frase2}", formando um PALÍNDROMO ')
else:
    print(f'A frase "{frase}" ao contrário é "{frase2}" e NÃO FORMA um palíndromo')