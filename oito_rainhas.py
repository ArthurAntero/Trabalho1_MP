def TabuleiroEh8x8(entrada):
    linhas = len(entrada)
    if linhas != 8:
        return -1
    for i in range(len(entrada)):
        colunas = len(entrada[i])
        if colunas != 8:
            return -1
    return 'ok'

def Tem_8_Rainhas(entrada):
    count_rainhas = 0
    for i in enumerate(entrada):
        for j in enumerate(entrada[i[0]]):
            if j[1] == 1:
                count_rainhas += 1
    if count_rainhas != 8:
        return -1
    return 'ok'

def Apenas_0_e_1(entrada):
    for i in enumerate(entrada):
        for j in enumerate(entrada[i[0]]):
            if j[1] != 1 and j[1] != 0:
                return -1
    return 'ok'