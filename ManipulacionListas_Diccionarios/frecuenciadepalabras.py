#Crear una función que cuente cuántas veces aparece cada palabra en un texto y devuelva un diccionario 
#con los resultados (ignorando mayúsculas/minúsculas y signos de puntuación).

frase = "El sol sale por el sol. La luna espera, pero el sol no espera."
palabras = []
palabra_actual = ""
signos_puntuacion = {'.', ',', ';', ':', '¡', '!', '¿', '?'}  

for caracter in frase:
    if caracter == " ":  
        if palabra_actual:  
            palabras.append(palabra_actual)
            palabra_actual = ""  
    elif caracter in signos_puntuacion:  
        continue
    else:
        palabra_actual += caracter.lower()  

print(palabras)

def contar_palabras():
    frecuencias = {}
    for i in palabras:
        print(i)
        if i not in frecuencias:
            frecuencias[i] = 1
        else:
            frecuencias[i] += 1
        
    return frecuencias

print(contar_palabras())
            
            
            
        


       
        


            
        
        
