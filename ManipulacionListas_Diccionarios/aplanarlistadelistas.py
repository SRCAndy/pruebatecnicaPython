#Aplanar una lista de listas (ej: [[1, 2], [3, 4]] → [1, 2, 3, 4]).

lista_gigante = [[1,2],[3,4]]
lista_aplanada = []
for sublista in lista_gigante:
    for elemento in sublista:
        lista_aplanada.append(elemento)
        
      
print(lista_aplanada)
    
