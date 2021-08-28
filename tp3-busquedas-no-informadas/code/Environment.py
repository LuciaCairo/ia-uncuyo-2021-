# El entorno está compuesto por una grilla de 100x100. 
# Los obstáculos se generan al azar. 
# Entorno completamente observable, determinista y estático

import random;
import numpy as np;
import math;

class Environment:

    #Constructor
    def __init__(self):
        self.sizeX = 100 #Dimension de la grilla (matriz)
        self.sizeY = 100 #Dimension de la grilla (matriz
        self.init_posX = random.randint(0,(self.sizeX - 1)); #Coordenada de poscicion inicial
        self.init_posY = random.randint(0,(self.sizeY - 1)); #Coordenada de poscicion inicial
        self.finish_posX = random.randint(0,(self.sizeX - 1)) #Coordenada de poscicion final
        self.finish_posY = random.randint(0,(self.sizeY - 1)); #Coordenada de poscicion final
        self.obstacles = int(self.sizeX * self.sizeY * 0.3) #Cantidad de obstaculos        
        self.grilla = np.zeros((self.sizeX, self.sizeY)); #Creo la grilla como una matriz de ceros (donde 0 = sin obstaculo)
        self.grilla[self.init_posX][self.init_posY] = 2 #(marco la posicion inicial con 2)
        self.grilla[self.finish_posX][self.finish_posY] = 3 #(marco la posicion final con 3)

        #Se distribuyen los obstaculos al azar
        self.distribute_obstacles();

    # Funcion donde se generan los obstáculos al azar   
    def distribute_obstacles(self):
        obs = 0 
        while obs != self.obstacles:
            x = random.randint(0,(self.sizeX - 1));
            y = random.randint(0,(self.sizeY - 1));
            # Los obstaculos no se ponen donde haya ya un obstaculo, ni en la posicion inicial o final
            if self.grilla[x][y] == 0:
                self.grilla[x][y] = 1; #1 = casilla con obstaculo
                obs += 1   

    # Se muestra el entorno
    def print_environment(self):
        print("Environment")
        for i in range (self.sizeX): 
            g=[] 
            for j in range (self.sizeY):
                if i == self.init_posX and j == self.init_posY:
                    print("INIT|",end="");
                elif i == self.finish_posX and j == self.finish_posY:
                    print("END |",end="");
                elif(self.grilla[i][j] == 1): 
                    print("////|",end="");
                else: 
                    print("    |",end="");
            print("")              
    

    # Comprobar si se acepta la accion que se quiere realizar 
    def accept_action(self,action,x,y):
        if action == "up": #Si se quiere ir hacia arriba verificamos que no se salga de la grilla y que no haya un obstaculo
            if x > 0 and self.grilla[x-1][y]!= 1 :
                return True    
            return False
        elif action == "down": #Si se quiere ir hacia abajo verificamos que la aspiradora no se salga de la grilla
            if x < self.sizeX - 1 and self.grilla[x+1][y]!= 1:
                return True    
            return False
        elif action == "right": #Si se quiere ir a la derecha verificamos que la aspiradora no se salga de la grilla
            if y < self.sizeY - 1 and self.grilla[x][y+1]!= 1:
                return True  
            return False
        elif action == "left": #Si se quiere ir a la izquierda verificamos que la aspiradora no se salga de la grilla
            if y > 0 and self.grilla[x][y-1]!= 1:
                return True    
            return False
