import os
import csv
import pandas as pd
os.chdir("Datos")

ciudad = set()
Grafo = [[0 for i in range(48)] for j in range(48)]

datos = pd.read_csv("Datos vias Colombia.csv")
ciudad.update(datos["A"].tolist() + datos["B"].tolist())
ciudades = sorted(list(ciudad))
#print(ciudades)
for i in range(len(datos)):
    Grafo[ciudades.index(datos.iloc[i]["A"])][ciudades.index(datos.iloc[i]["B"])] = (datos.iloc[i]["KM"], datos.iloc[i]["Minutos"])
#print(str(Grafo[ciudades.index('Medellin')][ciudades.index('Pereira')][0]))

def carretera_unica(a,b):
    if Grafo[ciudades.index(a)][ciudades.index(b)] == 0:
        comprobante = "No hay una via entre las ciudades"
    else:
        comprobante = "La via entre " + a + " y " + b + " tiene " + str(Grafo[ciudades.index(a)][ciudades.index(b)][0]) +  " kilometros y un tiempo de recorrido de " + str(Grafo[ciudades.index(a)][ciudades.index(b)][1]) + " minutos" 
    return comprobante

def dijkstra(M, inicial, terminal): #definimos el algoritmo dijkstra como una función
    """
    Este algoritmo recibe una matriz de pesos M y un nodo inicial r, y devuelve
    una lista de predecesores y una lista de pesos, que representan una r-ramificación de
    caminos mínimos desde r a cada vértice del grafo.
    """
    
    # Definimos lo que usaremos:
    n = len(M)                          #n es la cantidad de vértices del grafo
    p: list[int] = [None]*n             #lista que contendrá la información de los predecesores
    l: list[int] = [float('inf')]*n     #lista que contendrá la información de los pesos
    l[inicial] = 0                            #peso del nodo inicial es 0
    p[inicial] = inicial                            #predecesor del nodo inicial es él mismo
    coloreado: list[bool] = [False]*n   #coloreamos un vértice cuando lo visitamos, inicialmente están sin colorear
    
    
    while False in coloreado:           #Mientras hayan vértices sin colorear (es decir, sin visitar)
        
        nocoloreados = [v for v in range(n) if not coloreado[v]]    #Los tomo
        u = min(nocoloreados, key=lambda i: l[i])                   #saco el de menor peso
        coloreado[u] = True                                         #lo coloreo
        
        for v in range(n):                                          #para cada vértice adyacente a u
            #Reviso si el peso de v es mayor que el peso de u mas el peso de la arista (u,v)
            if M[u][v] > 0 and l[v] > l[u] + M[u][v]:      
                #en caso de que sí, actualizo el peso de v 
                l[v] = l[u] + M[u][v]
                #y actualizo también su predecesor
                p[v] = u
            
    camino = []
    
    t = terminal
    camino.append(t)
    while p[t] != inicial:
        t = p[t]
        camino.append(t)
        
    camino.append(inicial)
        
    camino.reverse()
    
    return camino,l
def Dijkstra(Grafo,a,b,indice):
    #Camino mas corto por el indice que se especifico
    #print(Grafo) 
    Grafo1 = [[0 for i in range(48)] for j in range(48)]
    for i in range(48):
        for j in range(48):
            if Grafo[i][j] != 0:
                Grafo1[i][j] = Grafo[i][j][indice]
            
    camino, l = dijkstra(Grafo1, ciudades.index(a), ciudades.index(b))
    
    
    ruta = list(map(lambda i: ciudades[i],camino ))
    return ruta

def ruta_corta_kilometros(Grafo,a,b):
    indice = 0
    ruta = Dijkstra(Grafo,a,b,indice) #indice 0 de la tupla
    return ruta 

def ruta_corta_minutos(Grafo,a,b):
    indice = 1
    ruta = Dijkstra(Grafo,a,b,indice) #indice 1 de la tupla
    return ruta

comprobante = str(input("¿Desea saber si una ciudad esta conectada por una única carretera con otra?: "))

if comprobante == "si":
    a = str(input("ingrese una ciudad: "))
    b = str(input("ingrese otra ciudad: "))
    if a and b in ciudades:
     com = carretera_unica(a,b)
     print(com)
    else:
        print("Alguna de las cuidades especificadas no es valida")

comprobante = str(input("¿Desea saber el camino mas corto entre dos cuidades respecto a los kilometros?: "))
if comprobante == "si":
    a = str(input("ingrese una ciudad: "))
    b = str(input("ingrese otra ciudad: "))
    if a and b in ciudades:
     ruta = ruta_corta_kilometros(Grafo,a,b)
     print("La ruta mas corta en función de kilometros es",ruta)
    else:
        print("Alguna de las cuidades especificadas no es valida")

comprobante = str(input("¿Desea saber el camino mas corto entre dos cuidades respecto a los minutos?: "))
if comprobante == "si":
    a = str(input("ingrese una ciudad: "))
    b = str(input("ingrese otra ciudad: "))
    if a and b in ciudades:
     ruta = ruta_corta_kilometros(Grafo,a,b)
     print("La ruta mas corta en función de minutos es",ruta)
    else:
        print("Alguna de las cuidades especificadas no es valida")

