import json
import os

ARQUIVO_JSON = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

TAREFAS = carregar_tarefas()

def salvar_tarefa(lista_completa):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_completa, f, indent=4, ensure_ascii=False)