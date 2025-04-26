import json

contatos = []


def adicionar_contato(nome, telefone, email):
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(contato)
    salvar_contatos()
    print(f"Contato '{nome}' adicionado com sucesso!")


def salvar_contatos():
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)


def carregar_contatos():
    global contatos
    try:
        with open('contatos.json', 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = []


def buscar_contato(nome):
    encontrados = [contato for contato in contatos if nome.lower()
                   in contato['nome'].lower()]
    if encontrados:
        print("Contatos encontrados:")
        for contato in encontrados:
            print(
                f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato encontrado.")


def main():
    carregar_contatos()

    while True:
        print("\n1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            email = input("Email do contato: ")
            adicionar_contato(nome, telefone, email)
        elif opcao == '2':
            nome = input("Informe o nome do contato a buscar: ")
            buscar_contato(nome)
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
