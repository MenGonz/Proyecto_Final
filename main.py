import os
import csv
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
   
print(ciudades)         
print(Grafo)

    
