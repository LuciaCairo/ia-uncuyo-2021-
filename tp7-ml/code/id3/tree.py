import math
from T import*

def train_treeD(ejemplos,atribs,defecto):
    if len(ejemplos) == 0: # Si ejemplos está vacio entonces devolver por-defecto
        return defecto  
    c = misma_class(ejemplos)
    if c[0]: # Si todos los elementos de ejemplos tienen la misma clasificación entonces devolver la clasificación
        return c[1] 
    if len(atribs) == 0: # Si atribs está vacio entonces devolver VALOR-MAYORÍA(ejemplos)
        return valor_may(ejemplos)
    else: 
        mejor = elegir_atributo(atribs, ejemplos)
        tree = Tree(atribs[mejor]) # Un nuevo árbol de decisión con nodo raíz mejor
        v = lista_v(ejemplos, mejor) # Lista con los valores posibles del mejor atributo
        atribs.remove(atribs[mejor])
        for i in range(len(v)): # Para cada valor vi del mejor atributo
            ejemplosi = list() 
            for j in range(len(ejemplos)):
                if v[i] == ejemplos[j][mejor]:
                    ejemplosi.append(ejemplos[j])
            m = valor_may(ejemplosi)
            subarbol = train_treeD(ejemplosi,atribs,m)
            tree = Tree(subarbol)
        return tree


def misma_class(e):
    c = e[0][4]
    cont = 0
    for i in range(1, len(e)): 
        cont += 1
        if e[i][4] != c:
            break
    if cont == len(e):
        return (True,c)
    return((False,None))

def valor_may(e):
    if calc_yes(e) > calc_no(e):
        return "yes"
    return "no"

def calc_yes(e):
    cont = 0
    for i in range(len(e)):
        if e[i][4] == "yes":
            cont += 1
    return cont

def calc_no(e):
    cont = 0
    for i in range(len(e)):
        if e[i][4] == "no":
            cont += 1
    return cont    

def lista_v(e,at):
    l = list()
    l.append(e[0][at])
    for i in range(1, len(e)): 
        if e[i][at] not in l:
            l.append(e[i][at])
    return l

def elegir_atributo(a, e):
    p = calc_yes(e)
    n = calc_no(e)
    maxGanancia = 0
    ind = 0
    for at in range(len(a)-1): # Para cada atributo hago una lista de sus posibles valores
        v = lista_v(e,at)
        R = 0
        for i in range(len(v)): # Calculo los valores de cada vi de A
            pi = 0
            ni = 0
            for f in range(len(e)):  # Para cada ejemplo con valor vi en el atributo A se cuenta la cantidad de pi y ni
                if v[i] == e[f][at]:
                    if e[f][len(a)-1] == "yes":
                        pi += 1
                    else:
                        ni += 1
            if ni != 0 and pi != 0:
                R += ((pi+ni)/(p+n))*((-pi/(pi+ni))* math.log((pi/(pi+ni)),2) - (ni/(pi+ni))* math.log((ni/(pi+ni)),2))
        G = ((-p/(p+n))*math.log((p/(p+n)),2) - (n/(p+n))*math.log((n/(p+n)),2)) - R # Calculo la ganancia del atributo A
        if G > maxGanancia:
            maxGanancia = G
            ind = at              
    return ind
