frase=str(input('Digite uma frase:')).upper().strip()
print('A frase possui', frase.count('A'), 'letras A')
print('A posição de A é:', frase.find('A') +1)
print('A posição do último A é:', frase.rfind('A') +1)