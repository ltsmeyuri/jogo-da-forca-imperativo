import random

#Declaração de Variáveis Globais 
erros_cometidos = 0
letras_descobertas = []
letras_incorretas = []
limite_erros = 6
palavra_secreta = "cavalo"
jogador_atual = "Yuri"
modo_multiplayer = False

def processar_jogada(letra_digitada):
    '''
    Recebe a letra digitada, valida e atualiza o estado do jogo;
    Retorna o status da jogada pra GUI saber o que mostrar.
    '''
    global erros_cometidos, jogador_atual
    
    if len(letra_digitada)!=1 or not letra_digitada.isalpha():
        return "invalida"
    
    letra_digitada = letra_digitada.lower()

    if letra_digitada in letras_descobertas or letra_digitada in letras_incorretas:
        return "repetida"

    if letra_digitada in palavra_secreta:
        letras_descobertas.append(letra_digitada)
        status = "acerto"
    else:
        letras_incorretas.append(letra_digitada)
        erros_cometidos +=1
        status = "erro"
    
    if modo_multiplayer:
        if jogador_atual == "A":
            jogador_atual = "B"
        else:
            jogador_atual = "A"
    return status
        
def obter_estado_palavra():
    mascara = ''
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            mascara +=letra + " "
        else:
            mascara += "_ "
    return mascara.strip()


def inicializar_jogo(nova_palavra, multiplayer=False):
    global palavra_secreta, erros_cometidos, modo_multiplayer, jogador_atual
    palavra_secreta = nova_palavra
    erros_cometidos = 0
    letras_descobertas.clear()
    letras_incorretas.clear()

    modo_multiplayer = multiplayer

    if modo_multiplayer:
        jogador_atual = random.choice(["A", "B"])
    else:
        jogador_atual = "Jogador 1"
