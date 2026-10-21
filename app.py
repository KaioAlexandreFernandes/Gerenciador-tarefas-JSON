def exibir_menu():
    print("Gerenciador de tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n[Funcionalidade de adicionar em breve...]")
        elif opcao == "2":
            print("\n[Funcionalidade de listar em breve...]")
        elif opcao == "3":
            print("\nSaindo do programa")
            break
        else:
            print("\nOpção inválida")

if __name__ == "__main__":
    main()