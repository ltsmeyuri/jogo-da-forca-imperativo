import random

#Declaração de Variáveis Globais 
erros_A = 0
erros_B = 0
letras_descobertas = []
letras_incorretas = []
limite_erros = 6
palavra_secreta = "cavalo"
jogador_atual = "Yuri"
modo_multiplayer = False
pontuacao_A = 0
pontuacao_B = 0
def processar_jogada(palpite):
    '''
    Recebe o palpite do jogador, valida e atualiza o estado do jogo;
    Retorna o status da jogada pra GUI saber o que mostrar.
    '''
    global erros_A, erros_B, jogador_atual, pontuacao_B, pontuacao_A
    palpite = palpite.lower()
    if not palpite.isalpha() or len(palpite)==0:
        return "invalida"
        
    elif len(palpite)==1:

        if palpite in letras_descobertas or palpite in letras_incorretas:
            return "repetida"

        if palpite in palavra_secreta:
            letras_descobertas.append(palpite)
            status = "acerto"
            pontos_ganhos = palavra_secreta.count(palpite)
            if jogador_atual == "B":
                pontuacao_B += pontos_ganhos
            else:
                pontuacao_A +=pontos_ganhos

        else:
            letras_incorretas.append(palpite)
            if jogador_atual == "B": 
                erros_B +=1
            else:
                erros_A +=1
            status = "erro"
        
        if modo_multiplayer:
            if jogador_atual == "A":
                jogador_atual = "B"
            else:
                jogador_atual = "A"
        return status
    else:
        if palpite==palavra_secreta:
            if modo_multiplayer and jogador_atual=="A":
                return "venceuA"
            elif modo_multiplayer and jogador_atual=="B":
                return "venceuB"
            else:
                return "venceu"
        else:
            if modo_multiplayer and jogador_atual=="B":
                return "venceuA"
            elif modo_multiplayer and jogador_atual=="A":
                return "venceuB"
            else: 
                return "perdeu"





        
def obter_estado_palavra():
    '''
    Cria a máscara com relação a palavra escolhida no banco e a retorna.
    '''
    mascara = ''
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            mascara +=letra + " "
        else:
            mascara += "_ "
    return mascara.strip()


def inicializar_jogo(nova_palavra, multiplayer=False):
    '''
    Reseta os status das variáveis que permeiam o jogo.
    '''
    global palavra_secreta, erros_A, erros_B, modo_multiplayer, jogador_atual, pontuacao_A, pontuacao_B
    palavra_secreta = nova_palavra
    erros_A = 0
    erros_B = 0
    pontuacao_A=0
    pontuacao_B=0
    letras_descobertas.clear()
    letras_incorretas.clear()

    modo_multiplayer = multiplayer

    if modo_multiplayer:
        jogador_atual = random.choice(["A", "B"])
    else:
        jogador_atual = "Jogador 1"
