# Definindo o número de filas e colunas
NUM_FILAS = 5
NUM_COLUNAS = 5

# Inicializando o mapa de assentos
mapa_assentos = [['D' for _ in range(NUM_COLUNAS)] for _ in range(NUM_FILAS)]


def visualizar_mapa():
    print("Mapa de Assentos:")
    for i, fila in enumerate(mapa_assentos):
        print(f"Fila {i + 1}: ", end="")
        for assento in fila:
            print(assento, end=" ")
        print()


def reservar_assento(fila, coluna):
    if mapa_assentos[fila][coluna] == 'D':
        mapa_assentos[fila][coluna] = 'R'
        print(
            f"Assento na fila {fila + 1}, coluna {coluna + 1} reservado com sucesso!")
    else:
        print("Esse assento já está reservado.")


def cancelar_reserva(fila, coluna):
    if mapa_assentos[fila][coluna] == 'R':
        mapa_assentos[fila][coluna] = 'D'
        print(
            f"Reserva na fila {fila + 1}, coluna {coluna + 1} cancelada com sucesso!")
    else:
        print("Esse assento não está reservado.")


def main():
    while True:
        print("\n1. Visualizar Mapa de Assentos")
        print("2. Reservar Assento")
        print("3. Cancelar Reserva")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            visualizar_mapa()
        elif opcao == '2':
            fila = int(input("Informe a fila (1 a 5): ")) - 1
            coluna = int(input("Informe a coluna (1 a 5): ")) - 1
            if 0 <= fila < NUM_FILAS and 0 <= coluna < NUM_COLUNAS:
                reservar_assento(fila, coluna)
            else:
                print("Fila ou coluna inválida.")
        elif opcao == '3':
            fila = int(input("Informe a fila (1 a 5): ")) - 1
            coluna = int(input("Informe a coluna (1 a 5): ")) - 1
            if 0 <= fila < NUM_FILAS and 0 <= coluna < NUM_COLUNAS:
                cancelar_reserva(fila, coluna)
            else:
                print("Fila ou coluna inválida.")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Definindo o número de filas e colunas
NUM_FILAS = 5
NUM_COLUNAS = 5

# Inicializando o mapa de assentos
mapa_assentos = [['D' for _ in range(NUM_COLUNAS)] for _ in range(NUM_FILAS)]


def visualizar_mapa():
    print("Mapa de Assentos:")
    for i, fila in enumerate(mapa_assentos):
        print(f"Fila: {fila}")
