# Implementar un agente reflexivo simple para el entorno de la aspiradora.

import random;

class Agent: 

    #Contructor
    def __init__(self,env): 
        # Recibe como parámetro un objeto de la clase Environment
        self.env = env 
        self.life = 1000 #Configurada para realizar mil movimientos
     
          
    # Accion de ir hacia arriba
    def up(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("up") and self.life > 0:
            self.env.init_posX -= 1 # Se mueve hacia arriba
            self.life -= 1 # Se resta una vida
            print("El agente se movio hacia arriba")
        else:
            print("No se puede realizar la accion")    

    # Accion de ir hacia abajo
    def down(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("down") and self.life > 0:
            self.env.init_posX += 1 # Se mueve hacia abajo
            self.life -= 1 # Se resta una vida
            print("El agente se movio hacia abajo")
        else: 
            print("No se puede realizar la accion")    

    # Accion de ir hacia la derecha
    def right(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("right") and self.life > 0:
            self.env.init_posY += 1 # Se mueve a la derecha
            self.life -= 1 # Se resta una vida
            print("El agente se movio a la derecha")
        else:
            print("No se puede realizar la accion")    

    # Accion de ir hacia la izquierda
    def left(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("left") and self.life > 0:
            self.env.init_posY -= 1 # Se mueve a la izquierda
            self.life -= 1 # Se resta una vida
            print("El agente se movio a la izquierda")
        else: 
            print("No se puede realizar la accion")  

    # Accion de limpiar o aspirar
    def suck(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("suck") and self.life > 0:
            self.env.grilla[self.env.init_posX][self.env.init_posY] = 0 # Se limpia 
            self.life -= 1 # Se resta una vida
            print("El agente aspiro")
        else:
            print("La cuadricula no esta sucia")       

    # Accion que no hace nada
    def idle(self):
        # Primero vemos si es posible realizar la accion
        if self.env.accept_action("idle") and self.life > 0:
            self.life -= 1 # Se resta una vida
            print("El agente no hizo nada")   

    # Sensa el entorno (me parece que esta de mas esta funcion)
    def perspective(self,env): 
        return self.env.is_dirty() #True si el entorno esta sucio

    # Implementa acciones a seguir por el agente
    def think(self):
        # Si el agente se encuentra en una casilla sucia, la limpiara
        if self.env.is_dirty(): 
            self.suck()
        else: # Si la cuadricula no esta sucia, el agente se movera en una direccion posible al azar y asi ira recorriendo el entorno.
            actions = ['up', 'down', 'left', 'right', 'idle']
            n = random.randint(0,len(actions)-1)
            if actions[n] == 'up':
                self.up()
            elif actions[n] == 'down':
                self.down()
            elif actions[n] == 'left':
                self.left()
            elif actions[n] == 'right':
                self.right()
            else:
                self.idle()

    
    #Implementa acciones aleatorias a seguir por el agente

    def aleatorio(self):
        act = ['up', 'down', 'left', 'right', 'idle','suck'] # Posibles acciones.
        n = random.randint(0,len(act)-1)
        if act[n] == 'up':
            self.up()
        elif act[n] == 'down':
            self.down()
        elif act[n] == 'left':
            self.left()
        elif act[n] == 'right':
            self.right()
        elif act[n] == 'suck':
            self.suck()   
        else:
            self.idle()
            
