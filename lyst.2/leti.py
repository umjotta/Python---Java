import json
from datetime import datetime

ARQUIVO_TAREFAS = 'tarefas.json'


def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    try:
        with open(ARQUIVO_TAREFAS, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO_TAREFAS, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def adicionar_tarefa(tarefas, descricao, prazo):
    """Adiciona uma nova tarefa à lista."""
    tarefa = {
        'descricao': descricao,
        'prazo': prazo,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)


def listar_tarefas(tarefas):
    """Lista as tarefas ordenadas por prazo."""
    tarefas_ordenadas = sorted(
        tarefas, key=lambda x: datetime.strptime(x['prazo'], '%Y-%m-%d'))
    for i, tarefa in enumerate(tarefas_ordenadas, start=1):
        status = '✔️' if tarefa['concluida'] else '❌'
        print(
            f"{i}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - Status: {status}")


def marcar_tarefa_concluida(tarefas, indice):
    """Marca uma tarefa como concluída."""
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido.")


def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo (YYYY-MM-DD): ")
            adicionar_tarefa(tarefas, descricao, prazo)
            print("Tarefa adicionada com sucesso!")

        elif opcao == '2':
            listar_tarefas(tarefas)

        elif opcao == '3':
            listar_tarefas(tarefas)
            indice = int(
                input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            marcar_tarefa_concluida(tarefas, indice)
            print("Tarefa marcada como concluída!")

        elif opcao == '4':
            print("Saindo do gerenciador de tarefas.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
