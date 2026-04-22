# 21/01/2026

# Exemplos com o comando for

# Mostre na tela todos os números múltiplos de 7 entre 1 e 1000

# 1° modo:
for n in range(1, 1001): #  [1, 2, 3, 4, 5...... 1000]    if n % 7 == 0:
        print(n)

# 2 ° modo
for n in range(7, 1001, 7):
    print(n)

for n in range(1001, 0, -7):
    print(n)

# Imprima na tela, entre 1 e 10000, todos os números pares e múltiplos de 12

for num in range(1, 10000):
    if num % 12 == 0:
        print(num)

#
for num in range(12, 10001, 12):
    print(num)

# Mostre todos os múltiplos de 3 e ímpares entre 1 e 10000:
for num in range(3, 10001, 3):
    if num % 2 != 0:
        print(num)

#
frutas = ["banana", "maçã", "cacau", "laranja", "kiwi", "pêssego", "côco", "manga", "maracujá"]
# Dada a lista acima mostre todas as frutas em letras maiúscula
# Mostre depois outra listagem somente das frutas que não possuem a letra "a"
# 1
for fruta in frutas:
    print(fruta.upper())

# 2
for fruta in frutas:
    if "a" not in fruta:
        print(fruta)

# Mostre agora somente as frutas que comecem com a letra "m":
# 1° modo
for fruta in frutas:
    if "m" in fruta[0]:
        print(fruta)

for fruta in frutas:
    if fruta.startswith("m"):
        print(fruta.upper())

#################################################################
palavras = [

    ["cachorro", "gato", "pássaro", "peixe", "tartaruga"],
    ["computador", "teclado", "mouse", "monitor", "impressora"],
    ["brasil", "portugal", "espanha", "frança", "alemanha"],
    ["vermelho", "azul", "verde", "amarelo", "preto"],
    ["caneta", "lápis", "borracha", "caderno", "mochila"],
    ["sol", "lua", "estrela", "planeta", "galáxia"],
    ["carro", "moto", "bicicleta", "caminhão", "ônibus"],
    ["alegria", "tristeza", "raiva", "medo", "surpresa"],
    ["praia", "montanha", "floresta", "rio", "oceano"],
    ["churrasco", "feijoada", "pizza", "sushi", "hambúrguer"],
    ["telefone", "celular", "tablet", "roteador", "internet"],
    ["futebol", "vôlei", "basquete", "natação", "tênis"],
    ["janela", "porta", "parede", "telhado", "chão"],
    ["chocolate", "sorvete", "bolo", "pudim", "doce"],
    ["chuva", "neve", "vento", "trovão", "relâmpago"]
]

print("\n*** ANÁLISE DE UMA LISTA DE PALAVRAS\n")
print(f"Qtd de palavras: {len(palavras)}")
# Dada a lista de palavras acima, mostre em tela somente as palavras que tenham a letra "u"
for linha in palavras:
    for palavra in linha:
        if "u" in palavra:
            print(palavra.title())

# Traga também a posição de cada palavra com a letra "u" dentro da matriz.
# Exemplo: "Neve" -> [14][1]

# Usaremos o for e o range() para percorrer cada palavras através do índice matricial
print("\n\n EXEMPLO 2 \n\n")
for linha in range(len(palavras)):  # Percorrendo linhas
    for coluna in range(len(palavras[linha])):  # Percorrendo colunas
        palavra = palavras[linha][coluna]
        if "u" in palavra:
            print(f"{palavra.title()} --> [{linha}][{coluna}]")


# 17/01/2026
# Refaça a atividade 9 substituindo o comando while pelo comando for:

# 2 - Crie um programa em Python que faça o cadastro de modelos de celulares.
# O cadastro deve conter modelo, marca e preço.
# O cadastro será finalizado quando o usuário digitar "sair" no nome do modelo.
# Após o cadastro dos modelos o programa deverá receber o valor máximo que um cliente pode pagar
# em um celular (via input()).
#
# Mostre na tela somente os celulares que possuem valor igual ou abaixo do valor que o cliente pode pagar.
celulares = []
print("\n*** RECOMENDAÇÃO DE CELULARES ***\n")
while True:  # Loop principal
    while True:  # Validação do modelo
        modelo = input("\nDigite o modelo do celular: ").strip().title()
        if len(modelo) < 3:
            print("\nModelo inválido!")
        else:
            break  # Tudo ok! Fim da validação do modelo!
    if modelo == "Sair":
        break
    while True:  # Validação da marca
        marca = input("\nDigite a marca do celular: ").strip().title()
        if len(marca) < 3:
            print("\nMarca inválida!")
        else:
            break  # Tudo ok! Fim da validação da marca!
    while True:
        try:
            preco = float(input("\nDigite o preço do celular: "))
            if preco <= 0:
                print("\nValor inválido!")
                # raise Exception
            else:
                break  # Fim da validação do preço!
        except Exception:
            print("\nSomente números são aceitos!")
    # Após validar os dados, faremos a inclusão na lista:
    celulares.append([modelo, marca, preco])
    print(f"\n{modelo} cadastrado com sucesso!")
if not celulares:
    print("\nNenhum modelo disponível!")
else:
    # Verificando poder de compra do cliente:
    while True:  # Validação do input de quanto o usuário pode pagar:
        try:
            poder_compra = float(input("\nDigite o valor máximo que você pode pagar: ").replace(",", "."))
            if poder_compra <= 0:
                raise Exception
            else:
                break  # Fim da validação do pode de compra do cliente
        except Exception:
            print("\nValor inválido!")
    # Percorrendo valores dos celulares
    i = 0
    encontrou = False  # Variável será usada para verificar se pelo menos 1 modelo está no orçamento
                       # do cliente
    # while i < len(celulares):  # Valor dos celulares será verificado um por um através do while e if
    #     if celulares[i][2] <= poder_compra:
    #         print(f"Modelo: {celulares[i][0]:12} | Marca: {celulares[i][1]:12} | "
    #               f"Preço: {celulares[i][2]:,.2f}")
    #         encontrou = True
    #     i = i + 1
    for celular in celulares:
        if celular[2] <= poder_compra:
            print(f"Modelo: {celular[0]:12} | Marca: {celular[1]:12} | Preço: {celular[2]:,.2f}")
            encontrou = True
    if not encontrou:
        print(f"\nNenhum modelo disponível até R$ {poder_compra:,.2f}  :( ")

# Crie um programa que faça cadastros de automóveis (NÃO será necessário validar dados).
# O cadastro deve conter: modelo, fabricante, ano e preço
# O programa será instalado em uma rede de garagens automotivas.
# O cadastro será finalizado quando o usuário digitar "sair".
# Ao final mostre todos os modelos cadastrados e o valor total na garagem.
# Use, para manipular a estrutura de dados, o comando for

print("\n\nGARAGEM SENAI RP \n\n")
veiculos = []  # Lista para armazenas os veículos cadastrados
while True:
    modelo = input("\nDigite o modelo do carro: ").upper()
    if modelo == "SAIR":
        break  # Fim do cadastro
    fabric = input(f"Digite o fabricante do {modelo}: ").upper()
    ano = int(input(f"fDigite o ano do {modelo}: "))
    preco = float(input(f"Digite o preço do {modelo}: "))
    veiculos.append([modelo, fabric, ano, preco])
    print(f"\n{modelo} cadastrado com sucesso!")
#
if not veiculos:
    print("\nNenhum veículo cadastrado!")
else:
    print("\n\n*** MODELOS DISPONÍVEIS ***\n\n")
    total = 0
    for v in veiculos:
        print(f"Modelo: {v[0]:12} | Fabric: {v[1]:12} | Ano: {v[2]} | Preço: {v[3]:,.2f}")
        total = total + v[3]
    print(f"\nValor total na garagem: R$ {total:,.2f}")
print("\nFim de programa!")
