# A) Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.
# https://replit.com/@LuciaCaro/IA-Trabajo-Practico-4#main.py

from Environment import *
from Agent import *
import random
import queue

for i in range (30):
    t = Environment()
    #t.print_environment()
    a = Agent(t)
    print(len(a.A_estrella()))
