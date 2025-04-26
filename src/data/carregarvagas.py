import json
import os

def carregar_vagas():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'vaga.json')

    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo {caminho_arquivo} não encontrado!")
        return None

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            vagas = json.load(file)
            return vagas
    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON!")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None