import os
import csv
import pandas as pd

os.chdir("Datos")

ciudades = set()
Grafo = [[None] * 49] * 49

datos = pd.read_csv("Datos vias Colombia.csv")
ciudades.update(datos["A"].tolist() + datos["B"].tolist())
print(ciudades)
 
    

def carretera_unica(a,b):
    comprobante=True
    return comprobante

def ruta_corta_kilometros(a,b):
    ruta=None #indice 0 de la tupla
    return ruta

def ruta_corta_minutos(a,b):
    ruta=None #indice 1 de la tupla
    return ruta



