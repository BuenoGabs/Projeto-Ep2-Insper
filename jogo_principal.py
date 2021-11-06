from dev1 import *
import random

texto_inicial = '''
Insper Dominó
=> Design de Software
Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.
Vamos começar!!!
'''
print(texto_inicial)

n_jogadores = int(input('Quantos jogadores? [2/4]'))
continuar = True 
while continuar:
    pecas = cria_pecas()
    status = inicia_jogo(n_jogadores, pecas)
    nao_ganhador = True
    while nao_ganhador:
        for i in range(n_jogadores):
            if i == 0:
                mao_jogador = status['jogadores'][0]
                lista_mesa =  status['mesa']
                posicoes = posicoes_possiveis(lista_mesa, mao_jogador)
                quantidade = len(mao_jogador)
                print('MESA: ', lista_mesa)
                print(f'Você tem {quantidade} peça(s)')
                escolha_do_jogador = input('Escolha a peça: ')

            
                




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if verifica_ganhador(jogadores) != -1:
        continuar == False
