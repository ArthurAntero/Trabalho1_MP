def TabuleiroEh8x8(entrada):
    linhas = len(entrada)
    if linhas != 8:
        return -1
    else:
        for i in range(len(entrada)):
            colunas = len(entrada[i])
            if colunas != 8:
                return -1
    return 'ok'