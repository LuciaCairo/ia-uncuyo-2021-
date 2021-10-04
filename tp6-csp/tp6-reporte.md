### 1. Describir en detalle una formulación CSP para el Sudoku.

**Variables:** Posciciones de las casillas

**Dominios:** {1,2,3,4,5,6,7,8,9}

**Restriccion:** Las variables que se encuentren casillas en la misma fila, columna o region no pueden tener el mismo valor.

### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

Ejecutamos los pasos del algoritmo.

Comenzamos con la asignación parcial, {WA=red, V=blue}

![image](https://user-images.githubusercontent.com/88351747/135920252-71e4ad09-0dea-4868-801b-62726a312c7e.png)

Se modifican los dominios

![image](https://user-images.githubusercontent.com/88351747/135920483-4e61dfd9-d921-4326-b7d2-80ec36e45dea.png)

![image](https://user-images.githubusercontent.com/88351747/135920936-dc1b52ce-00d8-4047-a289-1fd889d8e3cc.png)

![image](https://user-images.githubusercontent.com/88351747/135924678-6e8ea5c4-c8a8-46a9-86ef-873766343a77.png)

![image](https://user-images.githubusercontent.com/88351747/135924854-73845bc6-5fc9-4207-9266-f81de1a1639f.png)


Podemos ver que Q y NSW quedan sin valores consistentes si uno toma el rojo, no hay arcoconsistencia. Entonces se puede decir que el algoritmo detecta la inconsistentencia en la asignacion parcial.


### 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

En un arbol estructurado solo habra un arco para conectar las variables ya que solo hay una restriccion, por lo tanto el peor caso sera O(numero de aristas * tamaño del dominio)

### 4. AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco (Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O((n**2)*(d**2))

Se busca no procesar innecesariamente las aristas por lo que se procesan previamente las restricciones, entonces para cada valor de Xi se analizan las opciones de Xk para los que hay consistencia y se van reduciendo las posibilidades al eliminar los valores no legales de Xi.

### 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 

a) Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)

b) Argumentar por qué lo demostrado en a es suficiente. 

### 6. Implementar una solución al problema de las n-reinas utilizando una formulación CSP

**Backtracking:**

Tiempos: [0.13, 0.07, 5, 100, 345]

Estados:[233, 335028, 355273, 685863, 2395]

**Forward checking:** 

Tiempos: [0, 0, 0, 1.1, 1.2]

Estados: [80, 123, 222, 467, 1009]




