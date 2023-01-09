"""
Arquivo de testes do problema das 8 rainhas
"""

from oito_rainhas import tabuleiro_eh_8x8
from oito_rainhas import tem_8_rainhas
from oito_rainhas import apenas_0_e_1
from oito_rainhas import apenas_1_rainha_por_linha

def teste_tabuleiro_eh_8x8():
    """
    Teste da função que verifica se o tabuleiro é 8x8.
    """
    entrada_8x8 = [[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_9x8 = [[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_7x8 = [[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0]]
    entrada_8x9 = [[0,0,0,0,1,0,0,0,0],
                    [0,1,0,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0],
                    [0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,1,0,0,0],
                    [1,0,0,0,0,0,0,0,0]]
    entrada_nao_quadrada = [[0,0,0,0,1,0,0,0,0],
                            [0,1,0,0,0,0,0,0],
                            [0,0,0,1,0,0,0,0],
                            [0,0,0,0,0,0,1,0],
                            [0,0,1,0,0,0,0,0],
                            [0,0,0,0,0,0,0,1],
                            [0,0,0,0,0,1,0,0],
                            [1,0,0,0,0,0,0,0]]
    assert tabuleiro_eh_8x8(entrada_8x8) != -1
    assert tabuleiro_eh_8x8(entrada_9x8) == -1
    assert tabuleiro_eh_8x8(entrada_7x8) == -1
    assert tabuleiro_eh_8x8(entrada_8x9) == -1
    assert tabuleiro_eh_8x8(entrada_nao_quadrada) == -1

def teste_tem_8_rainhas():
    """
    Teste da função que verifica se o tabuleiro possui 8 rainhas.
    """
    entrada_8rainhas = [[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0]]
    entrada_7rainhas = [[0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0]]
    entrada_9rainhas = [[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,1]]
    assert tem_8_rainhas(entrada_8rainhas) != -1
    assert tem_8_rainhas(entrada_7rainhas) == -1
    assert tem_8_rainhas(entrada_9rainhas) == -1

def teste_apenas_0_e_1():
    """
    Teste da função que verifica se o tabuleiro possui apenas 0's e 1's.
    """
    entrada_valida =[[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_invalida = [[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,7,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0]]
    assert apenas_0_e_1(entrada_valida) != -1
    assert apenas_0_e_1(entrada_invalida) == -1

def teste_apenas_1_rainha_por_linha():
    """
    Teste da função que verifica se cada linha possui 1 rainha
    """
    entrada_valida =[[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_invalida = [[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0]]
    assert apenas_1_rainha_por_linha(entrada_valida) != 0
    assert apenas_1_rainha_por_linha(entrada_invalida) == 0
