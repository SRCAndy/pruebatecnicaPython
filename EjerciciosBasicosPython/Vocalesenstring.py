#Contar las vocales en una cadena de texto.

vocales = ['a','e','i','o','u']
frase = "esta frase es de prueba esperemos que el ejercicio nos funcione"
def contar_vocales():
    contador = 0
    for i in frase:
        if i in vocales:
            contador += 1 
    return[contador]

print(contar_vocales())
            
        