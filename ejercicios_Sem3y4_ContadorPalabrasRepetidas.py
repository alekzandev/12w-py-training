import click
from collections import Counter

@click.command()
@click.option('--texto', default = '' ,prompt = 'Introduce un texto', type = str)



def text_frecuency (texto):
    
    
    texto = texto.lower()
    texto = texto.replace(","," ")
    texto = texto.split()
    diccionario = dict()
    numrepetidas_lista = list()
    
    for i in texto:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
        
        
        
    for i in diccionario:
        numrepetidas_lista = diccionario[i]
        
    
        
    for j in diccionario:
        print(f"La palabra  --> ||  {j}  -->  {diccionario[j]}")
    #print(f"Las palabras repetidas estan en el siguiente diccionario ", diccionario)
    
if __name__ == '__main__':
    text_frecuency()