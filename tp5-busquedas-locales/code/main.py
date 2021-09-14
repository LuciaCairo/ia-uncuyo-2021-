# https://replit.com/@LuciaCaro/IA-Trabajo-Practico-5#main.py
from Environment import *
from Agent import *
import random
import numpy as np;
import time

# Implementar un algoritmo de Hill Climbing para resolver el problema de las n-reinas.
#for i in range (1):
#    t = Environment()
#    print('Estado inicial:')
#    t.print_environment()
#    print('Costo estado inicial: '+str(t.h(t.table))+'')
#    a = Agent(t)
#    print('Estados recorridos: '+str(a.Hill_Climbing())+'')
#    inicio = time.time()
#    print(a.Hill_Climbing())
#    final = time.time()
#    print(f" {round(final - inicio, 1)} seg")
#    print('-------------------------------------------')

# Implementar un algoritmo de Simulated Annealing para resolver el problema de las n-reinas.
#for i in range (1):
#    t = Environment()
    #print('Estado inicial:')
    #t.print_environment()
    #print('Costo estado inicial: '+str(t.h(t.table))+'')
#    a = Agent(t)
#    inicio = time.time()
#    a.Simulated_Annealing()
#    final = time.time()
#    print(f" {round(final - inicio, 1)} seg")
#    print(a.Simulated_Annealing())
#    print('-------------------------------------------')

# Implementar un Algoritmo Genético para resolver el problema de las n-reinas.
for i in range (30):
    t = Environment()
    # Creo la poblacion inicial
    poblacion = []
    for i in range(50):
        c = []
        for j in range(0,t.size):
            c.append(j) 
        a = np.zeros(t.size); 
        for i in range (0, t.size):
            n = random.randint(0,(t.size - i - 1));
            a[i] = c.pop(n)   
        poblacion.append(a) 
#    print('Poblacion inicial:')
#    for j in range(0,len(poblacion)):
#        print(''+str(j+1)+') '+str(poblacion[j])+'')
    a = Agent(t)
#    inicio = time.time()
    a.Algoritmo_Genetico(poblacion)
#    final = time.time()
#    print(f" {round(final - inicio, 1)} seg")
#    print('-------------------------------------------')
