"""
Arquivo de implementação do problema das 8 rainhas
"""
def tabuleiro_eh_8x8(entrada):
    """
    Função que verifica se o Tabuleiro é 8x8.
    """
    linhas = len(entrada)
    if linhas != 8:
        return -1
    for i in enumerate(entrada):
        colunas = len(entrada[i[0]])
        if colunas != 8:
            return -1
    return 'ok'

def tem_8_rainhas(entrada):
    """
    Função que verifica se a entrada dada possui 8 rainhas.
    """
    count_rainhas = 0
    for i in enumerate(entrada):
        for j in enumerate(entrada[i[0]]):
            if j[1] == 1:
                count_rainhas += 1
    if count_rainhas != 8:
        return -1
    return 'ok'

def apenas_0_e_1(entrada):
    """
    Função que verifica se a entrada fornecida possui apenas 0's e 1's.
    """
    for i in enumerate(entrada):
        for j in enumerate(entrada[i[0]]):
            if j[1] != 1 and j[1] != 0:
                return -1
    return 'ok'
