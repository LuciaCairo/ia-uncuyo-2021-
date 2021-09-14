# El programa deberá devolver el tablero solución (únicamente la estructura que representa el tablero). Junto a la cantidad de estados que tuvo que recorrer para llegar a la solución. En caso de alcanzar el máximo de estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H

import random;
from math import e;
import numpy as np;

class Agent: 

    #Contructor
    def __init__(self,env): 
        # Recibe como parámetro un objeto de la clase Environment
        self.env = env

    # Algoritmo Hill Climbing para resolver problema de las n-reinas.     
    def Hill_Climbing(self):
        cont = 0 # Variable que establezca el número máximo de estados que podrán ser evaluados.
        costo_actual = self.env.h(self.env.table) # Costo del estado actual del tablero
        costo_menor = costo_actual 
        while cont <= 100 and costo_menor != 0 :
            # Evaluamos los estados vecinos
            for c in range ( 0, self.env.size):
                vecino = self.env.table.copy()
                for f in range ( 0, self.env.size):
                    vecino[c] = f
                    costo_vecino = self.env.h(vecino)
                    if costo_vecino < costo_actual: # Encontramos un estado vecino con menor costo que el actual 
                        if costo_vecino < costo_menor: 
                            costo_menor = costo_vecino
                            estado_sig = vecino.copy()
                        if costo_vecino == costo_menor: # Para costos menores iguales elegimos aleatoriamente
                            n = random.randint(0,1)
                            if n == 0:
                                costo_menor = costo_vecino
                                estado_sig = vecino.copy()
            # Si no se encontro un estado mejor, se termina el problema y se devuelve el estado con menor h(t) 
            if costo_actual == costo_menor: # No se encontraron mejores estados que el actual
                break
            else: # Se encontro un estado mejor
                costo_actual = costo_menor
                self.env.table = estado_sig[:]
                cont += 1            
        return cont

    # Determina el valor de T como una función de tiempo (debe disminuir).
    def schedule(self, t):
        return t**(-2) + 0.3;

    # Algoritmo Simulated Annealing para resolver problema de las n-reinas.     
    def Simulated_Annealing (self):
        cont = 0 # Variable que establezca el número máximo de estados que podrán ser evaluados.
        costo_actual = self.env.h(self.env.table) # Costo del estado actual del tablero
        t = 1 # Tiempo inicial
        T = 100
        while cont <= 1000 and T != 0 and costo_actual != 0:
            T = self.schedule(t) # Temperatura inicial
            # Elegimos un estado vecino al azar
            vecino = self.env.table.copy()
            c = random.randint(0,self.env.size - 1)
            vecino[c] = random.randint(0,self.env.size - 1)
            # Calculo su costo
            costo_vecino = self.env.h(vecino)
            if costo_vecino < costo_actual: #Si el costo del estado vecino es menor que el costo del estado actual se acepta
                self.env.table = vecino
                costo_actual = costo_vecino
                cont += 1
            else: #Si el costo del estado vecino es mayor que el costo del estado actual se acepta con cierta probabilidad
                delta_e = costo_vecino - costo_actual
                t += 1 
                probabilidad = e**(-(delta_e/T))
                if probabilidad >= 0.5:
                    self.env.table = vecino
                    costo_actual = costo_vecino
                    cont += 1                   
        return cont 


    # Calcula la cantidad de reinas no amenazadas
    def fitness(self,individuo,e):
        a = self.env.h(individuo)
        return (e - a) 

    # Devolvemos el mejor individuo de una poblacion segun la funcion fitness
    def best(self,poblacion,e):
        best_f = 0
        global m
        for i in range(0,len(poblacion)):
            c = self.fitness(poblacion[i],e)
            if best_f < c:
                best_f = c
                m = poblacion[i]
        return m          

    # Seleccion de padres
    def parents(self,poblacion,e):
        # Seleccionamos los padres con el método selectivo, en el que se desechan los individuos debajo de un umbral
        padre = None
        umbral = int(e * (0.7))
        while padre == None:
            # Se elige el padre aleatoriamente
            i = random.randint(0,len(poblacion)-1)
            # Si la funcion idonea supera el umbral se toma ese padre
            if self.fitness(poblacion[i],e) > umbral:
                padre = poblacion[i]
                return poblacion[i];

        

    # Funcion para realizar el cruzamiento de dos padres
    def cruzamiento(self,x,y):
        # Se elije el punto de cruce al azar
        l = random.randint(0, self.env.size - 1)
        # Se crea el hijo apartir de los dos padres
        h = np.zeros(self.env.size);
        for i in range (0,self.env.size):
            if i < l:
                h[i] =  x[i]
            else:
                h[i] =  y[i]
        return h        

    # Funcion para generar una mutacion aleatoria
    def mutacion(self,h):
        j = random.randint(0,self.env.size-1)
        h[j] = random.randint(0,self.env.size-1)
        return h

    # Algoritmo Genetico para resolver problema de las n-reinas. 
    def Algoritmo_Genetico(self, poblacion):
        # Calculamos el estado ideal o solucion del tablero dado
        estado_solucion = 0
        for i in range(0, self.env.size):
            estado_solucion += i  
        # La condicion de parada es que se recorran hasta 100 estados o hasta que se encontre un estado solucion
        # Tenemos en cuenta cual es el invididuo con mejor funcion fitness
        best_ind = self.best(poblacion,estado_solucion) 
        best_f = self.fitness(best_ind, estado_solucion)
        estados = 0  
        while estados < 1000 and best_f != estado_solucion:
            estados += 1     
            # Creamos la nueva poblacion; cada cruce de dos padres producen dos descendientes
            descendientes = 0
            hijos = []; 
            while descendientes < len(poblacion):
                x = self.parents(poblacion, estado_solucion)
                y = self.parents(poblacion, estado_solucion)
                if np.array_equal(x,y): #Si los padres son iguales se repite la operacion
                    continue
                h1 = self.cruzamiento(x,y)
                h2 = self.cruzamiento(y,x)
                descendientes += 1
                # Si el nuevo individuo producto del cruzamiento no es mejor, se le agrega una mutacion
                if self.fitness(h1, estado_solucion) < best_f:
                    h = self.mutacion(h1)
                if self.fitness(h2, estado_solucion) < best_f:
                    h = self.mutacion(h2)    
                # Voy guardando los hijos
                if self.fitness(h1, estado_solucion) > self.fitness(h2, estado_solucion):
                    hijos.append(h1)
                else:
                    hijos.append(h2)
            # Añado los hijos a la poblacion    
            poblacion = hijos[:]
            # Tenemos en cuenta cual es el invididuo con mejor funcion fitness
            best_ind = self.best(poblacion,estado_solucion)
            best_f = self.fitness(best_ind, estado_solucion)    
        return estados
