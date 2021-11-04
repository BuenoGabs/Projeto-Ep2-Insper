# Função para criar as peças
def cria_pecas():
    from random import shuffle
    lista_domin = []
    for x in range (0,7):
        for y in range(0, 7):
            l = [x,y]
            lista_invert = [y,x]
            if lista_invert not in lista_domin:
                lista_domin.append(l)
    shuffle(lista_domin)
    return lista_domin

# Função para iniciar o jogo
def inicia_jogo(n,p):
    dicionario={'jogadores':{},'monte':[],'mesa':[]}
    for elemento in range(0,n):
        lista = []
        for x in range(0,7):
            lista.append(p[0])
            del p[0]
        dicionario['jogadores'][elemento] = lista
    dicionario['monte'] = p
    return dicionario

# Função para verificar o ganhador
def verifica_ganhador(dic):
    for i,valor in dic.items():
        if len(valor) == 0:
            return i 
    return -1         

# Função para somar peças
def soma_pecas(lista_pecas):
    lista_total = []
    for x in lista_pecas:
        for y in x:
            lista_total.append(y)
    total = sum(lista_total)
    return total

# Função para adicionar a peça na mesa
def adiciona_na_mesa(p, lista_mesa):
    if lista_mesa == []:
        lista_mesa.append(p)
    else:
        p_inicial = lista_mesa[0]
        p_final = lista_mesa[-1]
        n_inicial = p_inicial[0]
        n_final = p_final[1]
        p_invert = p[::-1]
        if p[1] == n_inicial: #comparando o lado direito n_i
            lista_mesa.insert(0, p)
        elif p_invert[1] == n_inicial: #comparando o lado direito n_i
            lista_mesa.insert(0, p_invert) 
        elif p[0] == n_final: #comparandoo lado esquerdo n_f
            lista_mesa.append(p) 

        elif p_invert[0] == n_final:
            lista_mesa.append(p_invert) 
    
    return lista_mesa