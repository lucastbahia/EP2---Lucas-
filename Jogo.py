def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    return posicoes


