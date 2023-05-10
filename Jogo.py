def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    return posicoes


def preenche_frota(frota, navio, linha, coluna,orientacao, tamanho):
    lista = []
    if orientacao == 'vertical':
        for i in range(0, tamanho):
            lista.append([linha + i, coluna])

    if orientacao == 'horizontal':
        for i in range(0, tamanho):
            lista.append([linha, coluna + i])

    if navio in frota and lista != []:
        frota[navio] += [lista]

    if navio not in frota and lista != []:
        frota[navio] = [lista]

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(infos_navios):
    tabuleiro = []
    for i in range(0,10):
        lista = []
    
        for i in range(0,10):
            lista.append(0)
        tabuleiro.append(lista)

    for posicoes in infos_navios.values():
        for posicao in posicoes:
            for posicao_exata in posicao:
                tabuleiro[posicao_exata[0]][posicao_exata[1]] = 1
    return tabuleiro

def afundados(frota,tabuleiro):
    X = 0
    for nome in frota.keys():
        for lugares in frota[nome]:
            Y = 0
            for lugar in lugares:
                if tabuleiro[lugar[0]][lugar[1]] == 'X':
                    Y += 1

            if Y == len(lugares):
                X += 1

    return X


def afundados(frota, tabuleiro):
    soma=0
    for tipo_navio in frota:
        for navio in frota[tipo_navio]:
            afundado=True
            for lugar in navio:
                if tabuleiro[lugar[0]][lugar[1]]!='X':
                    afundado=False
            if afundado==True:
                soma+=1
    return soma



def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha+i)
            posicao.append(coluna)
            lista.append(posicao)

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha)
            posicao.append(coluna+i)
            lista.append(posicao)
    return lista

    
def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    novas_embarcacoes = define_posicoes (linha, coluna, orientacao,tamanho)
    for i in novas_embarcacoes:
        if i[0] > 9 or i[1] > 9 or i[0]<0 or i[1]<0:
            return False
    for definicoes in frota. values ():
        embarcacoes_qtd = len (definicoes)
        for c in range(0, embarcacoes_qtd):
            embarcacao = definicoes [c]
            for i in novas_embarcacoes:
                if i in embarcacao:
                    return False
    return True
