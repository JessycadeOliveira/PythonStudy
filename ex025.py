nome=str(input('Qual o seu nome completo?')).strip()
print(f'Esse nome tem Silva?', {'silva' in nome.lower()})
