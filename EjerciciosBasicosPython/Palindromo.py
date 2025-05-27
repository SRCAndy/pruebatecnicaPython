#Verificar si una palabra es un palíndromo.

palabra = "barbado"
lista=[]
def guardar_palabra():
    for i in palabra:
        lista.append(i)

guardar_palabra()

lista_nueva=[]
def nueva_palabra():
    cantidad_letras= len(lista)-1
    while cantidad_letras >= 0:
        lista_nueva.append(lista[cantidad_letras])
        cantidad_letras -= 1

nueva_palabra()

print(lista == lista_nueva)

        






        


