# EJERCICIO B 
## Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio, calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que fue posible). Presentar los resultados en un gráfico de barras.
### Búsqueda por Anchura

**Estados:** [6130, 583, 4773, 2272, 3785, 68, 2981, 176, 1071, 4158 , 2908, 2964, 2152, 3525, 4270, 4101, 3033, 5057, 3218, 5988, 4886, 6611, 2570, 4355, 5098, 3389, 4159, 6173, 2138, 1340]

**Media:** 3465

**Desviación estandar:** 1763

### Búsqueda por Profundidad limitada

**Estados:** [2064, 1095, 1717, 2220, 4965, 1822, 3474, 1063, 4581, 4547, 3718, 2291, 2207, 2245, 1683, 1545, 1508, 2254, 4054, 2803, 3690, 4690, 1611, 3210, 3421, 4401, 4714, 749, 4004, 2945, 2528 ]

**Media:** 2573

**Desviación estandar:** 1369

### Busqueda Uniforme

**Estados:** [4451, 1285, 4249, 956, 2075, 4776, 1851, 267, 4549, 1892, 3536, 3476, 4082, 5608, 4201, 3277, 3135, 3456, 6207,, 6750, 6758, 2040, 6704, 1140, 4632, 6369, 5735, 298, 5701, 234]

**Media:** 3774

**Desviación estandar:** 2006

# EJERCICIO C 
## Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.

Considero que el algoritmo en anchura (BFS) es el mas eficiente ya que representa uno de los que menos estados ejecuto, es optimo y completo. 

Apesar de que el DFS recorre menos estados, este varias veces no es optimo ya que no siempre el camino que se encuentra es el mas corto y no llega a la solucion cuando se cumple el limite de profundidad, ademas en este caso de tamaño de la grilla la diferencia de estados con el BFS no es grande.

Por otro lado el algoritmo de busqueda uniforme tiene muchos mas estados que los dos antes mencionados.
