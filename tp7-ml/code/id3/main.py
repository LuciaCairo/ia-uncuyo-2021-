from tree import*
import csv
import numpy as np

# Implementar un árbol de decisión de acuerdo al pseudo-código provisto en AIMA. 

tennis = open("tennis.csv")
ej = csv.reader(tennis)
ejemplos = list(ej)
a = ejemplos[0] 
atribs = []
for i in range(len(a)):
    atribs.append(a[i])
ejemplos.remove(a)
arbol = train_treeD(ejemplos,atribs,"no")
