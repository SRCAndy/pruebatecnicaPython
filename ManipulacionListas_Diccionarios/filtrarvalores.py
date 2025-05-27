#Filtrar números mayores que 10 en una lista.

import random

lista = []
def llenar_lista():
    for i in range(10):
        lista.append(random.randint(1,100))
        i += 1

llenar_lista()
print(lista)
lista_filtrada= []
def filtrar_lista():
    for i in lista:
        if i > 10:
            lista_filtrada.append(i)
        
filtrar_lista()
print(lista_filtrada)