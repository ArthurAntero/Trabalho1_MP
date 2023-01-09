"""
Arquivo de testes do problema das 8 rainhas
"""

from oito_rainhas import tabuleiro_eh_8x8
from oito_rainhas import tem_8_rainhas
from oito_rainhas import apenas_0_e_1
from oito_rainhas import apenas_1_rainha_por_linha
from oito_rainhas import apenas_1_rainha_por_coluna
from oito_rainhas import apenas_1_rainha_por_diagonal
from oito_rainhas import problema_das_8_rainhas

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
    assert tabuleiro_eh_8x8(entrada_8x8) is True
    assert tabuleiro_eh_8x8(entrada_9x8) is False
    assert tabuleiro_eh_8x8(entrada_7x8) is False
    assert tabuleiro_eh_8x8(entrada_8x9) is False
    assert tabuleiro_eh_8x8(entrada_nao_quadrada) is False

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
    assert tem_8_rainhas(entrada_8rainhas) is True
    assert tem_8_rainhas(entrada_7rainhas) is False
    assert tem_8_rainhas(entrada_9rainhas) is False

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
    assert apenas_0_e_1(entrada_valida) is True
    assert apenas_0_e_1(entrada_invalida) is False

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
    assert apenas_1_rainha_por_linha(entrada_valida) is True
    assert apenas_1_rainha_por_linha(entrada_invalida) is False

def teste_apenas_1_rainha_por_coluna():
    """
    Teste da função que verifica se cada coluna possui 1 rainha
    """
    entrada_valida =[[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_invalida = [[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0]]
    assert apenas_1_rainha_por_coluna(entrada_valida) is True
    assert apenas_1_rainha_por_coluna(entrada_invalida) is False

def teste_apenas_1_rainha_por_diagonal():
    """
    Teste da função que verifica se cada diagonal possui 1 rainha
    """
    entrada_valida =[[0,0,0,0,1,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]
    entrada_invalida = [[0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0]]
    assert apenas_1_rainha_por_diagonal(entrada_valida) is True
    assert apenas_1_rainha_por_diagonal(entrada_invalida) is False

def teste_problema_das_8_rainhas():
    """
    Teste da função que testa o problema em geral
    """
    entrada_valida =[[0,0,0,0,1,0,0,0],
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
    entrada_7rainhas = [[0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0]]
    entrada_com_num_5 =   [ [0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,5,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0]]
    entrada_com_2_rainhas_na_linha = [  [0,0,0,0,1,0,0,0],
                                        [0,1,0,0,0,0,0,0],
                                        [0,0,0,1,0,0,0,0],
                                        [0,0,0,0,0,0,1,0],
                                        [0,0,1,0,0,0,0,0],
                                        [0,1,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [1,0,0,0,1,0,0,0]]
    entrada_com_2_rainhas_na_coluna = [ [1,0,0,0,0,0,0,0],
                                        [0,1,0,0,0,0,0,0],
                                        [0,0,0,1,0,0,0,0],
                                        [0,0,0,0,0,0,1,0],
                                        [0,0,1,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,1],
                                        [0,0,0,0,0,1,0,0],
                                        [0,0,0,0,0,0,0,1]]
    entrada_com_2_rainhas_na_diagonal = [   [0,0,0,0,0,0,0,1],
                                            [0,1,0,0,0,0,0,0],
                                            [0,0,0,1,0,0,0,0],
                                            [0,0,0,0,0,0,1,0],
                                            [0,0,1,0,0,0,0,0],
                                            [0,0,0,0,1,0,0,0],
                                            [0,0,0,0,0,1,0,0],
                                            [1,0,0,0,0,0,0,0]]
    assert problema_das_8_rainhas(entrada_valida) == 1
    assert problema_das_8_rainhas(entrada_9x8) == -1
    assert problema_das_8_rainhas(entrada_7rainhas) == -1
    assert problema_das_8_rainhas(entrada_com_num_5) == -1
    assert problema_das_8_rainhas(entrada_com_2_rainhas_na_linha) == 0
    assert problema_das_8_rainhas(entrada_com_2_rainhas_na_coluna) == 0
    assert problema_das_8_rainhas(entrada_com_2_rainhas_na_diagonal) == 0
