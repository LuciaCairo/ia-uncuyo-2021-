# El algoritmo deberá encontrar solo una solución para tableros de diferentes tamaños.
# Una posible estructura para el tablero es un arreglo, donde en cada posición hace referencia a una columna y cada valor a una fila.
# La función objetivo H(t) contabiliza la cantidad de pares de reinas amenazadas en el tablero t.

import random;
import numpy as np;
import math;

class Environment:

    #Constructor
    def __init__(self):
        self.size = 10 #Dimension del tablero  
        self.table = np.zeros(self.size); #Creo el tablero como un arreglo donde cada posición hace referencia a una columna y cada valor a una fila. 

        # Se distribuyen las reinas en cada columna al azar
        self.distribute_reinas();

    # Funcion donde se posicionan las reinas al azar, cada una en una columna
    def distribute_reinas(self):
        for c in range (0,self.size):
            f = random.randint(0,(self.size - 1));
            self.table[c] = None;
        return (self.table)
 

    # Se muestra el entorno
    def print_environment(self):
        print(self.table)


    # La función objetivo H(t) contabiliza la cantidad de pares de reinas amenazadas en el tablero t.
    def h(self,t):
        costo = 0
        # Evaluamos y contamos los pares de reinas amenzados
        for i in range ( 0, self.size):
            for c in range ( i+1, self.size):
                if t[i] == t[c]: #Si se encuentra que otra reina esta en la misma fila se suma uno a la cantidad de amenazadas
                    costo += 1
                else: #Si se encuentra que otra reina esta en la misma diagonal se suma uno a la cantidad de amenazadas
                    dif1 = abs(t[i] - t[c])
                    dif2 = abs(i - c)
                    if dif1 == dif2:
                        costo += 1 
        return costo
