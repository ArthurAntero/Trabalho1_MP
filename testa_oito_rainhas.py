from oito_rainhas import *

def teste_TabuleiroEh8x8():
    entrada_valida = [[0,0,0,0,1,0,0,0],
                      [0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0],
                      [0,0,0,0,0,0,1,0],
                      [0,0,1,0,0,0,0,0],
                      [0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0]]
    assert TabuleiroEh8x8(entrada_valida) != -1