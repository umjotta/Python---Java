usuarios = {
    'usuario1': {
        'senha': 'senha1',
        'saldo': 1000.0,
        'transacoes': []
    },
    'usuario2': {
        'senha': 'senha2',
        'saldo': 500.0,
        'transacoes': []
    }
}


def login():
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Login bem-sucedido!")
        return usuario
    else:
        print("Nome de usuário ou senha incorretos.")
        return None


def depositar(usuario):
    valor = float(input("Valor a depositar: "))
    usuarios[usuario]['saldo'] += valor
    usuarios[usuario]['transacoes'].append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")


def sacar(usuario):
    valor = float(input("Valor a sacar: "))
    if valor <= usuarios[usuario]['saldo']:
        usuarios[usuario]['saldo'] -= valor
        usuarios[usuario]['transacoes'].append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")


def exibir_saldo_transacoes(usuario):
    saldo = usuarios[usuario]['saldo']
    transacoes = usuarios[usuario]['transacoes']

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Histórico de Transações:")
    for transacao in transacoes:
        print(transacao)


def main():
    usuario_logado = login()

    if usuario_logado:
        while True:
            print("\n1. Depositar")
            print("2. Sacar")
            print("3. Exibir Saldo e Transações")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                depositar(usuario_logado)
            elif opcao == '2':
                sacar(usuario_logado)
            elif opcao == '3':
                exibir_saldo_transacoes(usuario_logado)
            elif opcao == '4':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Estrutura de dados para armazenar usuários
usuarios = {
    'usuario1': {
        'senha': 'senha1',
        'saldo': 1000.0,
        'transacoes': []
    },
    'usuario2': {
        'senha': 'senha2',
        'saldo': 500.0,
        'transacoes': []
    }
}


def login():
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Login bem-sucedido!")
        return usuario
    else:
        print("Tente novamente")
