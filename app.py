def exibir_menu():
    print("Gerenciador de tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")

def adicionar_tarefa(tarefas):
    titulo = input("\nDigite a descrição da tarefa: ").strip() # tirar os espaços
    if titulo:
        tarefas.append(titulo)  # jogar pro final da lista
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    else:
        print("A descrição não pode ser vazia.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def main():
    tarefas = []   # Lista aonde iremos guardar as tarefas

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nSaindo do programa")
            break
        else:
            print("\nOpção inválida")

if __name__ == "__main__":
    main()

