import os
import csv
import pandas as pd
os.chdir("Datos")

ciudad = set()
Grafo = [[0 for i in range(48)] for j in range(48)]

datos = pd.read_csv("Datos vias Colombia.csv")
ciudad.update(datos["A"].tolist() + datos["B"].tolist())
ciudades = sorted(list(ciudad))
print(ciudades)
for i in range(len(datos)):
    Grafo[ciudades.index(datos.iloc[i]["A"])][ciudades.index(datos.iloc[i]["B"])] = (datos.iloc[i]["KM"], datos.iloc[i]["Minutos"])
#print(str(Grafo[ciudades.index('Medellin')][ciudades.index('Pereira')][0]))

def carretera_unica(a,b):
    if Grafo[ciudades.index(a)][ciudades.index(b)] == None:
        comprobante = "No hay una via entre las ciudades"
    else:
        comprobante = "La via entre " + a + " y " + b + " tiene " + str(Grafo[ciudades.index(a)][ciudades.index(b)][0]) +  " kilometros y un tiempo de recorrido de " + str(Grafo[ciudades.index(a)][ciudades.index(b)][1]) + " minutos" 
    return comprobante

def Dijkstra(Grafo,a,b,indice):
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

comprobante = str(input(print("¿Desea saber si una ciudad esta conectada por una única carretera con otra?")))
if comprobante == "si":
    a = str(input(print("ingrese una ciudad")))
    b = str(input(print("ingrese otra ciudad")))
    if a and b in ciudades:
     com = carretera_unica(a,b)
     print(com)
    else:
        print("Alguna de las cuidades especificadas no es valida")

comprobante = str(input(print("¿Desea saber el camino mas corto entre dos cuidades respecto a los kilometros?")))
if comprobante == "si":
    a = str(input(print("ingrese una ciudad")))
    b = str(input(print("ingrese otra ciudad")))
    if a and b in ciudades:
     ruta = ruta_corta_kilometros(Grafo,a,b)
     print("La ruta mas corta en función de kilometros es",ruta)
    else:
        print("Alguna de las cuidades especificadas no es valida")

comprobante = str(input(print("¿Desea saber el camino mas corto entre dos cuidades respecto a los minutos?")))
if comprobante == "si":
    a = str(input(print("ingrese una ciudad")))
    b = str(input(print("ingrese otra ciudad")))
    if a and b in ciudades:
     ruta = ruta_corta_kilometros(Grafo,a,b)
     print("La ruta mas corta en función de minutos es",ruta)
    else:
        print("Alguna de las cuidades especificadas no es valida")

