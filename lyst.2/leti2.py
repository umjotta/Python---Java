import json

estoque = []


def adicionar_produto(nome, quantidade, preco):
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.append(produto)
    salvar_estoque()


def salvar_estoque():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)


def carregar_estoque():
    global estoque
    try:
        with open('estoque.json', 'r') as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        estoque = []


def exibir_estoque():
    total = 0
    print("Produtos no Estoque:")
    for produto in estoque:
        valor_produto = produto['quantidade'] * produto['preco']
        total += valor_produto
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")
