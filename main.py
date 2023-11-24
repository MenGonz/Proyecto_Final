import os
import csv
import pandas as pd

os.chdir("Datos")

ciudad = set()
Grafo = [[None] * 49] * 49

datos = pd.read_csv("Datos vias Colombia.csv")
ciudades.update(datos["A"].tolist() + datos["B"].tolist())
#print(ciudades)
 
os.chdir("..")
    

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


