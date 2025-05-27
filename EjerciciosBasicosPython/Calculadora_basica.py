#Implementar una calculadora sencilla (suma, resta, multiplicación, división) usando funciones.

def suma(a,b):
    sum = a + b
    return[sum]
    
def multiplicacion(a,b):
    mult = a * b 
    return[mult]
    
def resta(a,b):
    rest = a - b
    return[rest]

def division(a,b):
    div = a - b
    return[div]

def switchcase(c):
    if c == 1:
        a = int(input('Escribe 1 numero: '))
        b = int(input('Escribe 1 numero: '))
        print(f'su resultado es {suma(a,b)}')
    if c == 2:
        a = int(input('Escribe 1 numeros: '))
        b = int(input('Escribe 1 numero: '))
        print(f'su resultado es {multiplicacion(a,b)}')
    if c == 3:
        a = int(input('Escribe 1 numeros: '))
        b = int(input('Escribe 1 numero: '))
        print(f'su resultado es {resta(a,b)}')
    if c == 4:
        a = int(input('Escribe 1 numeros: '))
        b = int(input('Escribe 1 numero: '))
        print(f'su resultado es {division(a,b)}')
    
    if c > 4 or c > 1:
        print("Seleccion invalida, intenta de nuevo")
    
 
def main():
    c = int(input("Ecribe un numero dependiendo la operacion que deseas realizar 1.Suma 2.Multiplicacion 3.Resta 4.Division: "))
    switchcase(c)    

main()