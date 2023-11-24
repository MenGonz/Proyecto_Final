import os
import csv
os.chdir("Datos")
ciudades = set()
with open("Datos vias Colombia.csv") as f:
    lector = csv.reader(f)
    