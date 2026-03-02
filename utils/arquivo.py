import json
import os

CAMIHO_ARQUIVO = "data/clientes.json"

def garantir_clientes():
    """Cria o arquivo e a pasta se não existirem."""
    pasta = os.path.dirname(CAMIHO_ARQUIVO)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    if not os.path.exists(CAMIHO_ARQUIVO):
        with open(CAMIHO_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)

def ler_dados() -> list:
    """Lê os dados do arquivo JSON e retorna como uma lista."""
    garantir_clientes()
    with open(CAMIHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
    
def salvar_dados(dados: list) -> None:
    """Salva a lista de dados no arquivo JSON."""
    with open(CAMIHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)