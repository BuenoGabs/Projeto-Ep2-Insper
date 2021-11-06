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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if verifica_ganhador(jogadores) != -1:
        continuar == False
