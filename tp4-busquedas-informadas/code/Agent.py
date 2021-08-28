# Acciones : arriba, abajo, izq, der.
# El agente deberá ser capaz de resolver el problema planteado mediante un algoritmo de búsqueda A*.
# Al finalizar el proceso de formulación se deberán imprimir por pantalla: La matriz generada con los obstáculos y la secuencia de estados completa para llegar desde el estado inicial al estado destino (si es posible).

import random;
import queue;

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
            #print('up')
            return (p[0] - 1,p[1])
        #print('NO up')
        return None    

    # Accion de ir hacia abajo
    def down(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("down",p[0],p[1]):
            #print('down')
            return (p[0] + 1,p[1])
        #print('NO down')       
        return None

    # Accion de ir hacia la derecha
    def right(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("right",p[0],p[1]):
            #print('rigth')  
            return (p[0],p[1] + 1) 
        #print('NO rigth')   
        return None

    # Accion de ir hacia la izquierda
    def left(self,p):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("left",p[0],p[1]):
            #print('left')
            return (p[0],p[1] - 1) # Se mueve a la izquierda
        #print('NO left')
        return None    

    # Heurística admisible y consistente para el problema.  
    def h(self,x,y):
        a = abs(x - self.env.finish_posX); #Calculo la diferencia entre la posicion en X desde el nodo hasta el objetivo
        b = abs(y - self.env.finish_posY); #Calculo la diferencia entre la posicion en Y desde el nodo hasta el objetivo
        return (a + b) # Esta heuristica es admisible ya que ofrece un valor optimista que devuelve la menor cantidad de casillas que separan al nodo del objetivo sin tener en cuenta los obstaculos.


    # Funcion para calcular f(n) que es la suma de g(n) (coste del camino desde el nodo inicio al nodo n) y h(n)(coste estimado del camino más barato de n al objetivo)
    # En este problema en particular el valor de g siempre sera 1
    def f(self,g,h):
        return (g + h)
    
    # BUSQUEDA A*
    def A_estrella(self):
        h = self.h(self.pos_actualX,self.pos_actualY)
        node = (self.f(1,h),self.pos_actualX, self.pos_actualY) # Estado inicial
        frontera = queue.PriorityQueue() # Cola con prioridad donde cada elemento tiene la forma (f=g+h, poscicionX, posicionY)
        # Agrego el estado inicial
        frontera.put(node)
        explored = [] #Conjunto de explorados
        if node[1] == self.env.finish_posX and node[2] == self.env.finish_posY: # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados 
            return explored
        while frontera.empty() != True :
            node = frontera.get() # Se explora una casilla
            #print('Explorando:'+str(node)+'')
            explored.append(node)
            self.env.grilla[node[1]][node[2]] = 3 #Las casillas que se encentran marcadas con un 3 es porque fueron exploradas
            # Por cada posicion en la que se este, se pueden realizar 4 acciones (arriba, abajo, izq, der).
            actions = [self.up((node[1],node[2])),self.down((node[1],node[2])),self.left((node[1],node[2])),self.right((node[1],node[2]))]
            for i in range(4):
                child = actions[i] #Se ven los adyacentes a la casilla
                # Si el adyacente a la casilla fue None es porque la accion no se puede realizar ya sea porque se saldria del entorno o porque hay un obstaculo.
                # Tambien verificamos que este no este exploradro
                if child != None and self.env.grilla[child[0]][child[1]] != 3:
                    if child == (self.env.finish_posX,self.env.finish_posY): # Si llegamos al objetivo (la posicion final) se devuelven los estados explorados
                        return explored
                    else: #Si no esta el objetivo se agrega a la frontera para expandirlo despues
                        h = self.h(child[0], child[1])
                        node = (self.f(1,h), child[0], child[1])
                        frontera.put(node)
                        #print('Anadio a fontera:'+str(node)+'') 
        print('No hay solucion ')                     
        return []
