from lib.funcoes import *

def menu():
    print("=== Menu ===")
    print("1. Gerenciar Equipamentos")
    print("2. Gerenciar Salas")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_equipamentos()
        elif opcao == '2':
            gerenciar_salas()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()