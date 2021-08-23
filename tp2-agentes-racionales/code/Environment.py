# SIMULADOR QUE DETERMINA LA MEDIDA DE RENDIMIENTO PARA EL ENTORNO DE LA ASPIRADORA:
# Un punto por cada recuadro que limpia.
# Vida de 1.000 acciones.
# La dimensión de la grilla se conoce.
# No se conoce la distribución de la suciedad (aleatorio).
# No se conoce la localización inicial del agente (aleatorio).
# Las cuadrículas se mantienen limpias.
# Aspirando se limpia la cuadrícula.
# El agente se mueve , excepto que lo lleve fuera de la grilla.
# Acciones: arriba, abajo, izq, derecha, limpiar, NoHacerNada.
# El agente percibe su locación y si esta contiene suciedad.

import random;
import numpy as np;
import math;

class Environment:

    #Constructor
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX #Dimension de la grilla (matriz)
        self.sizeY = sizeY #Dimension de la grilla (matriz
        self.init_posX = init_posX #Coordenada de poscicion inicial
        self.init_posY = init_posY #Coordenada de poscicion inicial
        self.dirt_rate = dirt_rate #Porcentaje de suciedad
        self.cont_actions = 0 #Control de vida de 1000 acciones
        self.points = 0 #Puntos de la aspiradora
        self.dirty_boxes = (math.ceil((self.sizeX * self.sizeY) * self.dirt_rate)) #Cantidad de casillas sucias
        self.grilla = np.zeros((self.sizeX, self.sizeY));#Creo la grilla como una matriz de ceros (donde 0 = limpio)

        #Se distribuye la suciedad
        self.dirty();

    #Se ensucian aleatoriamente la cantidad de cuadriculas correspondiente    
    def dirty(self):
        d = 0 
        while d != self.dirty_boxes:
            x = random.randint(0,(self.sizeX - 1));
            y = random.randint(0,(self.sizeY - 1));
            if self.grilla[x][y] == 0:
                self.grilla[x][y] = 1; #1 = casilla sucia
                d += 1                 
    
    # Comprobar si se acepta la accion que se quiere realizar 
    def accept_action(self,action):
        if action == "up": #Si se quiere ir hacia arriba verificamos que la aspiradora no se salga de la grilla
            if self.init_posX > 0:
                return True    
            return False
        elif action == "down": #Si se quiere ir hacia abajo verificamos que la aspiradora no se salga de la grilla
            if self.init_posX < self.sizeX - 1:
                return True    
            return False
        elif action == "right": #Si se quiere ir a la derecha verificamos que la aspiradora no se salga de la grilla
            if self.init_posY < self.sizeY - 1:
                return True  
            return False
        elif action == "left": #Si se quiere ir a la izquierda verificamos que la aspiradora no se salga de la grilla
            if self.init_posY > 0:
                return True    
            return False
        elif action == "suck": #Si se quiere aspirar primero verificamos que la cuadricula este sucia 
            return self.is_dirty()
        elif action == "idle":
            return True #Si no se quiere hacer nada siempre se puede realizar esta accion.                
        else:
            print("Accion no reconocida") #Se inicio una accion no reconocida.
            return False

    # Verificacion de si la casilla esta sucia
    def is_dirty(self):
        if self.grilla[self.init_posX][self.init_posY] == 1:
            return True
        return False    
  
    # Rendimiento obtenido y cantidad de casillas que quedaron sucias
    def get_performance(self):
        dirty = 0;
        #Se recorre la grilla buscando cuantas casillas quedaron sucias
        for i in range (self.sizeX): 
            for j in range (self.sizeY): 
                if (self.grilla[i][j]):
                    dirty += 1;
        # Vemos cuantas casillas se limpiaron para contar los puntos de rendimiento      
        self.points = self.dirty_boxes - dirty
        print("Quedaron "+str(dirty)+" casillas sucias")
        print("Se aspiro "+str(self.points)+" casillas (puntos)")
        return self.points;

    # Se muestra el entorno
    def print_environment(self):
        print("Environment")
        for i in range (self.sizeX): 
            g=[] 
            for j in range (self.sizeY):
                if i == self.init_posX and j == self.init_posY:
                    print(" agent |",end="");
                elif(self.grilla[i][j] == 1): 
                    print(" dirty |",end="");
                else: 
                    print("       |",end="");
            print("")
            
