from banco import TAREFAS, salvar_tarefa
import os

def fluxo():
    os.system('cls')
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa ")
        print("4. Deletar Tarefa")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            editar_tarefa()
        elif escolha == "4":
            excluir_tarefa()
        else:
            print("Opção inválida. Tente novamente.")

def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório!")

def adicionar_tarefa():
    os.system('cls') 
    
    titulo = input_obrigatorio("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa(opcional): ") or "Sem descrição"
    status = input("A tarefa está concluída? (s/n): ").strip().lower()
    concluida = True if status == 's' else False
    
    nova_tarefa = {
        "id": len(TAREFAS) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida
    }
    
    TAREFAS.append(nova_tarefa)
    
    salvar_tarefa(TAREFAS) 
    print("Tarefa salva!")
    print("Apertar Enter para continuar...")
    input()

def listar_tarefas():
    os.system('cls') 
    if not TAREFAS:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("\n--- SUAS TAREFAS ---")
    for t in TAREFAS:
        status = "[X]" if t["concluida"] else "[ ]"
        print(f"{t['id']}. {status} {t['titulo']} - {t['descricao']}")
    print("Apertar Enter para continuar...")
    input()
    

def editar_tarefa():
    os.system('cls') 
    tarefa_id = int(input_obrigatorio("Digite o ID da tarefa que deseja editar: "))
    for tarefa in TAREFAS:
        if tarefa["id"] == tarefa_id:
            novo_titulo = input(f"Novo título (atual: {tarefa['titulo']}): ")
            nova_descricao = input(f"Nova descrição (atual: {tarefa['descricao']}): ")
            novo_status = input(f"A tarefa está concluída? (s/n) (atual: {'s' if tarefa['concluida'] else 'n'}): ").strip().lower()
            
            if novo_titulo:
                tarefa["titulo"] = novo_titulo
            if nova_descricao:
                tarefa["descricao"] = nova_descricao
            if novo_status in ['s', 'n']:
                tarefa["concluida"] = True if novo_status == 's' else False
            
            salvar_tarefa(TAREFAS)
            print("Tarefa atualizada!")
            print("Apertar Enter para continuar...")
            input()
            return
    print("Tarefa não encontrada.")
    print("Apertar Enter para continuar...")
    input()

def excluir_tarefa():
    os.system('cls') 
    tarefa_id = int(input_obrigatorio("Digite o ID da tarefa que deseja excluir: "))
    for i, tarefa in enumerate(TAREFAS):
        if tarefa["id"] == tarefa_id:
            del TAREFAS[i]
            salvar_tarefa(TAREFAS)
            print("Tarefa excluída!")
            print("Apertar Enter para continuar...")
            input()
            return
    print("Tarefa não encontrada.")
    print("Apertar Enter para continuar...")
    input()

fluxo()