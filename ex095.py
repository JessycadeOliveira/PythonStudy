jogadores = []
resp = "S"
while True:
    dados = {}
    dados['nome'] = str(input("Nome: "))
    dados["partidas"] = int(input("Quantidade de partidas: "))
    print("Quantos gols foram feitos em cada partida:")
    dados["gols"] = []
    for g in range(0, dados["partidas"]):
        dados["gols"].append(int(input(f"{g}° partida: ")))
    dados["total"] = sum(dados["gols"])
    jogadores.append(dados)
    resp = str(input("CONTINUA [S/N]: ")).upper().strip()[0]
    while resp not in "NS":
        print('ERRO!')
        print('TENTE NOVAMENTE...')
        resp = str(input("CONTINUA [S/N]: ")).upper().strip()[0]
    if resp in "N":
        break
# print(jogadores)
print("-" * 30)
print(f"{'cod.':<5} {'nome':>5} {'':>2}{'gols'} {'total':^15}")
print("—" * 39)
for j in enumerate(jogadores):
    print(f"{j[0]:.<1} {j[1]['nome']:>10} {'':>2}{j[1]['gols']} {j[1]['total']:^15}")

print("-" * 30)
print()
while True:
    j = int(input("Deseja ver informacões de qual jogador [999 pra parar]: "))
    print()
    if j == 999:
        print("<<<PROGRAMA ENCERRADO!>>>")
        break
    if j < (len(jogadores) - 1):
        print(f"Informações do jogador {jogadores[j]['nome']}!")
        for p, v in enumerate(jogadores[j]['gols']):
            print(f"{p}° partida, {v} gols.")
        print()
    elif j > (len(jogadores) - 1) and j != 999:
        print("Jogador não existente!")
        print('Tente novamente.')
        print()