#PROJETO 1.1

import winsound

sexo_masculino = "masculino", "m", "macho", "homem", "homi", "man"
sexo_feminino = "feminino", "f", "fêmea", "mulher", "muie", "muié", "girl"
print("-" * 80)

nomes = []
cidades = []

for i in range(3):

    nome = input("Nome completo? ").title().strip()
    print()
    sexo = input("Sexo? ").strip().lower()
    print()
    cidade = input("Cidade de residência? ").strip()
    print()
    nomes.append(nome)
    cidades.append(cidade)
    if sexo.split()[0].lower() in sexo_masculino:
        tratamento = "senhor"
    else:
        tratamento = "senhora"

    print("Perfeito, o seu cadastro foi finalizado com sucesso, {} {}.".format(tratamento, nome))
print()
print("-" * 60)

resposta = input("Deseja ver o conteúdo dos cadastros? ").strip().lower()

if resposta in ["sim", "s", "positivo", "pode ser"]:
    print("Nomes:{}".format(nomes))
    print()
    print("Cidades:{}".format(cidades))
    print()
    print("Certo, conversa encerrada")

else:
    (print("Certo, conversa encerrada"))
print()
print("-" * 30)
winsound.PlaySound("mp3xx1.wav", winsound.SND_FILENAME)
