import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def mostrar_menu():
    print("\n1. Adicionar Tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")

def listar_tarefas(tarefas):
    print("\nLista de tarefas:")
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t}")

def remover_tarefa(tarefas):
    try:
        num = int(input("Digite o número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def main():
    tarefas = carregar_tarefas()
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        match escolha:
            case "1":
                adicionar_tarefa(tarefas)
            case "2":
                listar_tarefas(tarefas)
            case "3":
                remover_tarefa(tarefas)
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção Inválida.")

if __name__ == "__main__":
    main()
