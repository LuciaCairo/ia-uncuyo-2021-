# El programa deberá devolver el tablero solución (únicamente la estructura que representa el tablero). Junto a la cantidad de estados que tuvo que recorrer para llegar a la solución. En caso de alcanzar el máximo de estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H

import random;
from math import e;
import numpy as np;

class Agent: 

    #Contructor
    def __init__(self,env): 
        # Recibe como parámetro un objeto de la clase Environment
        self.env = env      

    # Backtracking
    def Backtracking(self):
        return self.Backtracking_recursivo(self.env.size,0)

    def Backtracking_recursivo(self , n, e):
        if n == 0:
            return True
        for i in range(0, self.env.size):
            for j in range(0, self.env.size):
                e += 1
                c = True
                for r in range(0,self.env.size):
                    if r != i:
                        if self.env.table[r] == j:
                            c = False
                        dif1 = abs(self.env.table[i] - self.env.table[r])
                        dif2 = abs(i - r)   
                        if dif1 == dif2:
                            c = False
                if (c and (self.env.table[i]!=j)):
                    self.env.table[i]= j
                    if self.Backtracking_recursivo(n-1,e) == True:
                        return True                
        return e   
    

        # Forward Checking
        def Forward_Checking(self):
            p = random.randint(0 , (self.env.size - 1));
            self.env.table[0] = p # Posiciono la primer reina al azar
            no_asignadas = np.arange(1, self.env.size - 1)
            #l = np.zeros(self.size - 1);
            #for i in no_asignadas:
                # Se le deben asignar os valores del dominio legales a cada variable que queda sin asginar.
                # El algoritmo termina cuando no quedan elementos en el dominio consistentes para las variables que aun no han sido asignadas 
            return p    

        def legales(self, reina):
            p = np.arange(0, self.env.size - 1)
            for j in range (0 , self.env.size): # Se ve todo el dominio
                if j in self.env.table:
                    p.remove(j)    
                dif1 = abs(self.env.table[reina] - self.env.table[j])
                dif2 = abs(j - reina)
                if dif1 == dif2:
                    p.remove(j)   
            return p  
