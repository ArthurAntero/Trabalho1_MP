"""
Arquivo de implementação do problema das 8 rainhas
"""
import numpy as np

def tabuleiro_eh_8x8(entrada):
    """
    Função que verifica se o Tabuleiro é 8x8.
    """
    linhas = len(entrada)
    if linhas != 8:
        return False
    for i in enumerate(entrada):
        colunas = len(entrada[i[0]])
        if colunas != 8:
            return False
    return True

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
        return False
    return True

def apenas_0_e_1(entrada):
    """
    Função que verifica se a entrada fornecida possui apenas 0's e 1's.
    """
    for i in enumerate(entrada):
        for j in enumerate(entrada[i[0]]):
            if j[1] != 1 and j[1] != 0:
                return False
    return True

def apenas_1_rainha_por_linha(entrada):
    """
    Função que verifica se a entrada fornecida possui apenas 1 rainha por linha.
    """
    for i in enumerate(entrada):
        count_rainhas = i[1].count(1)
        if count_rainhas != 1:
            return False
    return True

def apenas_1_rainha_por_coluna(entrada):
    """
    Função que verifica se a entrada fornecida possui apenas 1 rainha por coluna.
    """
    coluna = 0
    while coluna < 8:
        lista_coluna = []
        for i in enumerate(entrada):
            lista_coluna.append(i[1][coluna])
        if lista_coluna.count(1) != 1:
            return False
        coluna += 1
    return True

def apenas_1_rainha_por_diagonal(entrada):
    """
    Função que verifica se a entrada fornecida possui apenas 1 rainha por diagonal
    """
    lista_diagonais = []
    for i in range(8):
        diagonal = np.diag(entrada, i)
        lista_diagonal = []
        for i_i in diagonal:
            lista_diagonal.append(i_i)
        lista_diagonais.append(lista_diagonal)
    for j in range(-1, -8, -1):
        diagonal = np.diag(entrada, j)
        lista_diagonal = []
        for j_j in diagonal:
            lista_diagonal.append(j_j)
        lista_diagonais.append(lista_diagonal)
    for diag in lista_diagonais:
        if diag.count(1) > 1:
            return False
    return True

def problema_das_8_rainhas(entrada):
    """
    Função que verifica se a entrada fornecida é válida, função principal do código
    """
    test1 = tabuleiro_eh_8x8(entrada)
    test2 = tem_8_rainhas(entrada)
    test3 = apenas_0_e_1(entrada)
    teste_entrada_valida = test1 and test2 and test3
    test4 = apenas_1_rainha_por_linha(entrada)
    test5 = apenas_1_rainha_por_coluna(entrada)
    test6 = apenas_1_rainha_por_diagonal(entrada)
    teste_solucao = test4 and test5 and test6
    if teste_entrada_valida and teste_solucao:
        return 1
    if teste_entrada_valida:
        return 0
    return -1
