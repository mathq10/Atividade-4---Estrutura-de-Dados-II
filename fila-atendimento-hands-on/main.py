import random

from fila import Fila
from fila_circular import FilaCircular
from fila_prioridade import FilaPrioridade


def criar_cliente(numero):
    prioridade = random.randint(1, 3)

    nomes = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro",
        "Rafael", "Sofia", "Thiago", "Victor", "Yasmin"
    ]

    return {
        "nome": nomes[numero - 1],
        "senha": f"A{numero:03d}",
        "prioridade": prioridade
    }


def mostrar_cliente(cliente):
    prioridade = {
        1: "Emergência",
        2: "Prioritário",
        3: "Normal"
    }

    print(
        f"Nome: {cliente['nome']} | "
        f"Senha: {cliente['senha']} | "
        f"Prioridade: {cliente['prioridade']} - "
        f"{prioridade[cliente['prioridade']]}"
    )


def gerar_clientes():
    return [criar_cliente(i) for i in range(1, 21)]


def mostrar_clientes(clientes):
    for cliente in clientes:
        mostrar_cliente(cliente)


# ==========================================================
# PARTE 1 - FILA CLÁSSICA
# ==========================================================

def executar_fila_classica(clientes):
    print("\n" + "=" * 60)
    print("FILA CLÁSSICA - FIFO")
    print("=" * 60)

    fila = Fila()

    for cliente in clientes:
        fila.enqueue(cliente)

    print("\nOrdem de atendimento:")

    while not fila.empty():
        cliente = fila.dequeue()
        print(f"{cliente['senha']} - {cliente['nome']}")


# ==========================================================
# PARTE 2 - FILA CIRCULAR
# ==========================================================

def executar_fila_circular(clientes):
    print("\n" + "=" * 60)
    print("FILA CIRCULAR")
    print("=" * 60)

    fila = FilaCircular(5)

    print("\nInserindo 5 clientes:")

    for cliente in clientes[:5]:
        fila.enqueue(cliente)
        fila.mostrar_estado()
        print()

    print("Removendo 2 clientes:")

    for _ in range(2):
        cliente = fila.dequeue()
        print(f"Atendido: {cliente['senha']} - {cliente['nome']}")
        fila.mostrar_estado()
        print()

    print("Inserindo novos clientes nas posições liberadas:")

    for cliente in clientes[5:7]:
        fila.enqueue(cliente)
        fila.mostrar_estado()
        print()


# ==========================================================
# PARTE 3 - FILA DE PRIORIDADE
# ==========================================================

def executar_fila_prioridade(clientes):
    print("\n" + "=" * 60)
    print("FILA DE PRIORIDADE")
    print("=" * 60)

    fila = FilaPrioridade()

    for cliente in clientes:
        fila.enqueue(cliente)

    print("\nOrdem de atendimento:")

    while not fila.empty():
        cliente = fila.dequeue()

        print(
            f"{cliente['senha']} - "
            f"{cliente['nome']} - "
            f"Prioridade {cliente['prioridade']}"
        )


# ==========================================================
# DESAFIO FINAL
# ==========================================================

def executar_desafio():
    clientes = gerar_clientes()

    print("\n" + "=" * 60)
    print("CLIENTES NA ORDEM DE CHEGADA")
    print("=" * 60)

    mostrar_clientes(clientes)

    executar_fila_classica(clientes)
    executar_fila_circular(clientes)
    executar_fila_prioridade(clientes)


# ==========================================================
# MENU INTERATIVO
# ==========================================================

def menu_interativo():
    fila = Fila()

    while True:
        print("\n" + "=" * 60)
        print("SISTEMA INTELIGENTE DE ATENDIMENTO")
        print("=" * 60)

        print("1 - Inserir cliente")
        print("2 - Atender próximo cliente")
        print("3 - Consultar próximo cliente")
        print("4 - Visualizar fila")
        print("5 - Tamanho da fila")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            senha = input("Senha: ")

            while True:
                try:
                    prioridade = int(
                        input(
                            "Prioridade (1-Emergência, "
                            "2-Prioritário, 3-Normal): "
                        )
                    )

                    if prioridade in [1, 2, 3]:
                        break

                    print("Digite uma prioridade entre 1 e 3.")

                except ValueError:
                    print("Digite um número válido.")

            cliente = {
                "nome": nome,
                "senha": senha,
                "prioridade": prioridade
            }

            fila.enqueue(cliente)

            print("Cliente inserido com sucesso!")

        elif opcao == "2":
            cliente = fila.dequeue()

            if cliente:
                print("\nCliente atendido:")
                mostrar_cliente(cliente)
            else:
                print("A fila está vazia.")

        elif opcao == "3":
            cliente = fila.head()

            if cliente:
                print("\nPróximo cliente:")
                mostrar_cliente(cliente)
            else:
                print("A fila está vazia.")

        elif opcao == "4":
            if fila.empty():
                print("A fila está vazia.")
            else:
                print("\nClientes aguardando atendimento:")
                for cliente in fila.clientes:
                    mostrar_cliente(cliente)

        elif opcao == "5":
            print(f"\nClientes na fila: {fila.size()}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    while True:
        print("\n" + "=" * 60)
        print("SISTEMA INTELIGENTE DE ATENDIMENTO")
        print("=" * 60)

        print("1 - Executar desafio completo")
        print("2 - Menu interativo")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            executar_desafio()

        elif opcao == "2":
            menu_interativo()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()