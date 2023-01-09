from oito_rainhas import *

def teste_TabuleiroEh8x8():
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
    assert TabuleiroEh8x8(entrada_8x8) != -1
    assert TabuleiroEh8x8(entrada_9x8) == -1
    assert TabuleiroEh8x8(entrada_7x8) == -1
    assert TabuleiroEh8x8(entrada_8x9) == -1
    assert TabuleiroEh8x8(entrada_nao_quadrada) == -1
    