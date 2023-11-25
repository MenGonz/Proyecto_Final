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

def ruta_corta_kilometros(Grafo,a,b):
    indice = 0
    ruta = Dijkstra(Grafo,a,b,indice) #indice 0 de la tupla
    return ruta 

def ruta_corta_minutos(Grafo,a,b):
    indice = 1
    ruta = Dijkstra(Grafo,a,b,indice) #indice 1 de la tupla
    return ruta

comprobante = str(print("¿Desea saber si una ciudad esta conectada por una única carretera con otra?"))
if comprobante == "si":
    a = str(print("ingrese una ciudad"))
    b = str(print("ingrese otra ciudad"))
    com = carretera_unica(a,b)
    if com:
        print("Existe una conexión directa")
    else:
        print("No existe una conexión directa")

comprobante = str(print("¿Desea saber el camino mas corto entre dos cuidades respecto a los kilometros?"))
if comprobante == "si":
    a = str(print("ingrese una ciudad"))
    b = str(print("ingrese otra ciudad"))
    ruta = ruta_corta_kilometros(Grafo,a,b)
    print(ruta)

comprobante = str(print("¿Desea saber el camino mas corto entre dos cuidades respecto a los minutos?"))
if comprobante == "si":
    a = str(print("ingrese una ciudad"))
    b = str(print("ingrese otra ciudad"))
    ruta = ruta_corta_minutos(Grafo,a,b)
    print(ruta)

