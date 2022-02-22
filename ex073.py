times= ('Flamengo', 'Vasco', 'Fluminense', 'Botafogo',
        'Corinthians', 'Madureira', 'Chapecoense','Santos',
        'Cruzeiro', 'Internacional')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(f'A lista de times participantes é: {sorted(times)}')
print(f' O time Chapecoense está na {times.index("Chapecoense")+1} posição')

