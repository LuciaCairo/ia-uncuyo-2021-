# Acciones : arriba, abajo, izq, der.
# El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:
# Búsqueda por Anchura
# Búsqueda por Profundidad limitada
# Busqueda Uniforme
# Al finalizar el proceso de formulación se deberán imprimir por pantalla: La matriz generada con los obstáculos y la secuencia de estados completa para llegar desde el estado inicial al estado destino (si es posible).

import random;

class Agent: 

    #Contructor
    def __init__(self,env): 
        # Recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.pos_actualX = self.env.init_posX
        self.pos_actualY = self.env.init_posY 
          
    # Accion de ir hacia arriba
    def up(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("up",p[0],p[1]):
            return (p[0] - 1,p[1])
        return None    

    # Accion de ir hacia abajo
    def down(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("down",p[0],p[1]):
            return (p[0] + 1,p[1])   
        return None

    # Accion de ir hacia la derecha
    def right(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("right",p[0],p[1]):
            return (p[0],p[1] + 1)     
        return None

    # Accion de ir hacia la izquierda
    def left(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("left",p[0],p[1]):
            return (p[0],p[1] - 1) # Se mueve a la izquierda
        return None    
            


    # BUSQUEDA POR ANCHURA
    def BFS(self):
        node = (self.pos_actualX, self.pos_actualY) # Estado inicial
        # Agrego el estado inicial
        frontera = [node] # Actuara como cola FIFO
        explored = [] #Conjunto de explorados
        if node == (self.env.finish_posX , self.env.finish_posY): # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados 
            return explored
        while len(frontera) != 0:
            node = frontera.pop(0) # Se explora una casilla
            explored.append(node)
            # Por cada posicion en la que se este, se pueden realizar 4 acciones (arriba, abajo, izq, der).
            actions = [self.up(node),self.down(node),self.left(node),self.right(node)]
            for i in range(4):
                child = actions[i] #Se ven los adyacentes a la casilla
                # Si el adyacente a la casilla fue None es porque la accion no se puede realizar ya sea porque se saldria del entorno o porque hay un obstaculo.
                # Tambien verificamos que este no este ya exploradro ni en la frontera
                if child != None and child not in frontera and child not in explored :
                    if child == (self.env.finish_posX,self.env.finish_posY): # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados
                        return explored
                    else: #Si no esta el objetivo se agrega a la frontera para expandirlo despues
                        frontera.append(child)             
        return []
 

    # BUSQUEDA POR PROFUNDIDAD LIMITADA
    def DFS(self,limit):
        node = (self.pos_actualX, self.pos_actualY) # Estado inicial
        profundidad = 0
        # Agrego el estado inicial
        frontera = [node] # Actuara como cola LIFO
        explored = [] #Conjunto de explorados
        if node == (self.env.finish_posX , self.env.finish_posY): # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados 
            return explored
        while len(frontera) != 0:
            node = frontera.pop(len(frontera)-1) # Se explora una casilla
            explored.append(node)
            if profundidad > limit: # Si se paso el limite en profundidad 
                return [ ]
            # Por cada posicion en la que se este, se pueden realizar 4 acciones (arriba, abajo, izq, der).
            actions = [self.up(node),self.down(node),self.left(node),self.right(node)]
            profundidad += 1
            for i in range(4):
                child = actions[i] #Se ven los adyacentes a la casilla
                # Si el adyacente a la casilla fue None es porque la accion no se puede realizar ya sea porque se saldria del entorno o porque hay un obstaculo.
                # Tambien verificamos que este no este ya exploradro ni en la frontera
                if child != None and child not in frontera and child not in explored :
                    if child == (self.env.finish_posX,self.env.finish_posY): # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados
                        return explored
                    else: #Si no esta el objetivo se agrega a la frontera para expandirlo despues
                        frontera.append(child) 
        return [ ]

    # BUSQUEDA UNIFORME
    def Uniform(self):
        node = (self.pos_actualX, self.pos_actualY, 1) # Estado inicial con costo 0
        # Agrego el estado inicial a la frontera
        frontera = [(self.pos_actualX, self.pos_actualY)]
        fronteraC = [node] # Actuara como cola con prioridad
        exploredC = [] #Conjunto de explorados
        explored = [] #Conjunto de explorados
        if node[0] == self.env.finish_posX and node[1] == self.env.finish_posY: # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados 
            return explored
        while len(frontera) != 0:
            # Se explora una casilla con menor costo -------------
            min = fronteraC[0][2]
            indice = 0
            for i in range (len(fronteraC)):
                if min > fronteraC[i][2]:
                    min = fronteraC[i][2]
                    indice = i        
            node = fronteraC.pop(indice)
            n = frontera.pop(indice)
            #---------------------------------------
            exploredC.append(node)
            explored.append(n)
            # Por cada posicion en la que se este, se pueden realizar 4 acciones (arriba, abajo, izq, der).
            actions = [self.up(node),self.down(node),self.left(node),self.right(node)]
            for i in range(4):
                c = actions[i] #Se ven los adyacentes a la casilla
                if c != None:
                    childC = (c[0],c[1],(node[2]+1))
                    child = (c[0],c[1])
                # Si el adyacente a la casilla fue None es porque la accion no se puede realizar ya sea porque se saldria del entorno o porque hay un obstaculo.
                # Tambien verificamos que este no este ya explorado ni en la frontera
                    if child not in frontera and child not in explored :
                        if child[0] == self.env.finish_posX and child[1] == self.env.finish_posY: # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados
                            return explored
                        else: #Si no esta el objetivo se agrega a la frontera para expandirlo despues
                            frontera.append(child)
                            fronteraC.append(childC)                  
        return []
