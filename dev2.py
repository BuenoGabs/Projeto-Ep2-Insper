#funções da academia
# criando peças do dominó
def cria_pecas():
    from random import shuffle
    lista_domin = []
    for x in range(0,7):
        for y in range(0,7):
            l = [x,y]
            lista_invert = [y,x]
            if lista_invert not in lista_domin:
                lista_domin.append(l)
    shuffle(lista_domin)
    return lista_domin

# iniciando o jogo de dominó
def inicia_jogo(n,p):
    dicionario = {'jogadores':{}, 'monte':[], 'mesa':[]}
    for elemento in range(0,n):
        lista =[]
        for x in range(0,7):
            lista.append(p[0])
            del p[0]
        dicionario['jogadores'][elemento]= lista
    dicionario['monte'] = p
    return dicionario

# quem ganhou no dominó
def verifica_ganhador(dic):
    for i, valor in dic.items():
        if len (valor) == 0:
            return i
    return -1

# soma peças no dominó
def soma_pecas(lista_pecas):
    lista_total = []
    for x in lista_pecas:
        for y in x:
            lista_total.append(y)
    total = sum(lista_total)
    return total

# posições possiveis das mãos
def posicoes_possiveis(lista_mesa, lista_pecas_mao):
    if lista_mesa == []:
        return list(range(len(lista_pecas_mao)))
    ponta_direita = lista_mesa[-1][1]
    ponta_esquerda = lista_mesa[0][0]
    lista_posicao = []
    for i in range(len(lista_pecas_mao)):
        peca = lista_pecas_mao[i]
        if peca[0] == ponta_direita or peca[0] == ponta_esquerda or peca[1] == ponta_direita or peca[1] == ponta_esquerda:
            lista_posicao.append(i)
    return lista_posicao

#adicionando peças na mesa
def adiciona_na_mesa(p, lista_mesa):
    if lista_mesa == []:
        lista_mesa.append(p)
    else:
        p_inicial = lista_mesa[0]
        p_final = lista_mesa[-1]
        n_inicial = p_inicial[0]
        n_final = p_final[1]
        p_invert = p[::-1]
        if p[1] == n_inicial: 
            lista_mesa.insert(0,p)
        elif p_invert[1] == n_inicial:
            lista_mesa.insert(0,p_invert)
        elif p[0] == n_final:
            lista_mesa.append(p)

        elif p_invert[0] == n_final:
            lista_mesa.append(p_invert)

    return lista_mesa

# jogo dominó:
from dev2 import *
import random

texto_inicial = '''
Insper Dominó
=> Design de Software
Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar 
sem peças na sua mão antes dos outros jogadores.
Vamos começar!!!
'''
print(texto_inicial)

n_jogadores = int(input('Quantos jogadores?[2/4]'))
continuar = True
while continuar:
    pecas = cria_pecas()
    status = inicia_jogo(n_jogadores, pecas)
    nao_ganhador = True
    while nao_ganhador:
        for i in range(n_jogadores):
            if i == 0:
                mao_jogador = status['jogadores'][0]
                lista_mesa = status['mesa']
                posicoes = posicoes_possiveis(lista_mesa, mao_jogador)
                qunatidade = len(mao_jogador)
                print(f'Você tem {qunatidade} peças(s)')
                escolha_do_jogador = input('Escolha a peça:')
        if verifica_ganhador(jogadores) != -1:
            continuar == False
