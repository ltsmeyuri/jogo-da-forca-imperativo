import json
import random
import os

ARQUIVO_PALAVRAS = 'palavras.json'
ARQUIVO_RANKING = 'ranking.json'

def carregar_palavras():
    
    """
    Lê o arquivo de palavras e retorna o dicionário completo.
    Retorna um dicionário vazio caso o arquivo não exista.
    """
    if not os.path.exists(ARQUIVO_PALAVRAS):
        return{}
    with open(ARQUIVO_PALAVRAS, 'r', encoding="utf-8") as arquivo:
        return json.load(arquivo)

def sortear_palavr(categoria, dificuldade):
    banco_palavras = carregar_palavras()

    if categoria in banco_palavras and dificuldade in banco_palavras[categoria]:
        lista = banco_palavras[categoria][dificuldade]
        if len(lista) > 0:
            return random.choice(lista)
    
    return None

def carregar_ranking():

    """
    Lê o arquivo de ranking.
    Retorna uma lista de dicionários com os dados dos jogadores.
    """

    if not os.path.exists(ARQUIVO_RANKING):
        return []
    
    with open(ARQUIVO_RANKING, 'r', encoding='utf-8') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_pontuacao(nome_jogador, pontuacao_final):
    ranking = carregar_ranking

    novo_registro = {
        "nome": nome_jogador,
        "pontos": pontuacao_final
    }

    ranking.append(novo_registro)

    # Ordena a lista pelos pontos
    ranking_ordenado = sorted(ranking, key=lambda jogador: jogador['pontos'], reverse=True)

    with open(ARQUIVO_RANKING, 'w', encoding='utf-8') as arquivo:
        json.dump(ranking_ordenado, arquivo, indent=4, ensure_ascii=False) 