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