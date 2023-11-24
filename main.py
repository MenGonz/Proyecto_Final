import os
import csv
import pandas as pd





os.chdir("Datos")
ciudades = set()
Grafo = [[None] * 49] * 49
with open("Datos vias Colombia.csv") as f:
    lector = csv.reader(f)
    for row in lector:
        ciudades.add(row[0])
        ciudades.add(row[1])
    ciudades.remove('')
    ciudades = sorted(list(ciudades))
    for row in lector:
        if row[0] in ciudades:
            arista = (row[2], row[3])
            Grafo[ciudades.index(row[0])][ciudades.index(row[1])] = arista
os.chdir("..")   


def carretera_unica(a,b):
    comprobante=True
    return comprobante

def ruta_corta_kilometros(a,b):
    ruta=None #indice 0 de la tupla
    return ruta

def ruta_corta_minutos(a,b):
    ruta=None #indice 1 de la tupla
    return ruta



