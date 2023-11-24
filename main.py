import os
import csv
import pandas as pd

os.chdir("Datos")

ciudad = set()
Grafo = [[None] * 49] * 49

datos = pd.read_csv("Datos vias Colombia.csv")
ciudad.update(datos["A"].tolist() + datos["B"].tolist())
ciudades = sorted(list(ciudad))
for i in range(len(datos)):
    Grafo[ciudades.index(datos.iloc[i]["A"])][ciudades.index(datos.iloc[i]["B"])] = (datos.iloc[i]["KM"], datos.iloc[i]["Minutos"])
    Grafo[ciudades.index(datos.iloc[i]["B"])][ciudades.index(datos.iloc[i]["A"])] = (datos.iloc[i]["KM"], datos.iloc[i]["Minutos"])

print(Grafo)

def carretera_unica(a,b):
    if Grafo[ciudades.index(a)][ciudades.index(b)] == None:
        comprobante = "No hay ninguna via entre las ciudades"
    else:
        comprobante = "La via entre " + a + " y " + b + " tiene " + Grafo[ciudades.index(a)][ciudades.index(b)][0] +  " kilometros y un tiempo de recorrido de " + Grafo[ciudades.index(a)][ciudades.index(b)][1] + " minutos" 
    return comprobante

def Dijkstra(matriz,a,b,indice):
    #Camino mas corto por el indice que se especifico 
    ruta = None 
    return ruta

def ruta_corta_kilometros(matriz,a,b):
    indice = 0
    ruta = Dijkstra(matriz,a,b,indice) #indice 0 de la tupla
    return ruta 

def ruta_corta_minutos(matriz,a,b):
    indice = 1
    ruta = Dijkstra(matriz,a,b,indice) #indice 1 de la tupla
    return ruta


