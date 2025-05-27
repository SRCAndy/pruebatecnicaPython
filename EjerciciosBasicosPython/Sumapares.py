#Crear una función que sume los números pares de una lista.

import random
list=[]
def crear_lista():
    for i in range(10):
        list.append(random.randint(1,100))
    return list
        
        
def mostrar_list():   
    for i in list:
        return[print(list)]

def suma_pares():
    for i in list:
         if i%2 == 0:
             sum = i

    return sum
crear_lista()
mostrar_list()
print(f'la suma de pares es:{suma_pares()}')
