from Environment import *
from Agent import *
import random;

# https://replit.com/@LuciaCaro/IA-Trabajo-Practico-2#main.py

# Ejercicio B ---------------------------------
#t = Environment(10,5,4,3,1);

#Probar acciones 
#print(t.accept_action("up"))
#print(t.accept_action("down"))
#print(t.accept_action("right"))
#print(t.accept_action("left"))
#print(t.accept_action("suck"))
#print(t.accept_action("idle"))
#print(t.accept_action("girar"))

#Probar
#print(t.grilla)
#t.print_environment()
#t.get_performance()

# Ejercicio C ---------------------------------
#agente = Agent(t)

#agente.up()
#t.print_environment()
#agente.down()
#t.print_environment()
#print(t.grilla)
#agente.left()
#agente.suck()
#agente.left()
#t.print_environment()
#agente.idle()
#agente.think()
#t.get_performance()
#t.print_environment()
#agente.think()
#agente.think()
#t.print_environment()

# Ejercicio D ---------------------------------
# Evaluar el desempeño del agente agente reflexivo para:
# Entorno de 2x2 
#t = Environment(2,2,random.randint(0,2-1),random.randint(0,2-1),0.8);
#agente = Agent(t)
#t.print_environment()
#while agente.life != 0:
#    agente.think()
#print("Vidas: "+str((agente.life)))
#print("Empiezan sucias: "+str(t.dirty_boxes))    
#t.get_performance()

# Entorno de 4x4 
#t = Environment(4,4,random.randint(0,4-1),random.randint(0,4-1),0.8);
#agente = Agent(t)
#t.print_environment()
#while agente.life != 0:
#    agente.think()
#print("Vidas: "+str((agente.life)))
#print("Empiezan sucias: "+str(t.dirty_boxes))    
#t.get_performance() 

t = Environment(128,128,random.randint(0,128-1),random.randint(0,128-1),0.8);
agente = Agent(t)
while agente.life != 0:
    agente.aleatorio()
print("Vidas: "+str((agente.life)))
print("Empiezan sucias: "+str(t.dirty_boxes))    
t.get_performance()
