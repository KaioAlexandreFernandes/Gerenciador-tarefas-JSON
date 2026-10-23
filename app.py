import json
import os  # verifica se o arquivo já existe no computador

ARQUIVOS_DADOS = "tarefas.json"

def exibir_menu():
    print("Gerenciador de tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")

def carregar_tarefas(): #Vai ler o arquivo JSON e retornar a lista que tem nele. Se não existir esse arquivo retorna uma lista vazia"""
    if os.path.exists(ARQUIVOS_DADOS):
        with open(ARQUIVOS_DADOS, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return[]

def salvar_tarefas(tarefas): #Salva a lista atual dentro do arquivo JSON
    with open(ARQUIVOS_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def adicionar_tarefa(tarefas):
    titulo = input("\nDigite a descrição da tarefa: ").strip() # tirar os espaços
    if titulo:
        tarefas.append(titulo)  # jogar pro final da lista
        salvar_tarefas(tarefas) # IRá salvar no arquivo assim que vc adicionar uma tarefa
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
        print("\n")

def main():
    tarefas = carregar_tarefas()   # Lista aonde iremos guardar as tarefas

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

