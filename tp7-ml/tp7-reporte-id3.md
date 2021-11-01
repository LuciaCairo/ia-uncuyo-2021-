# Investigar sobre las estrategias de los árboles de decisión para datos de tipo real y elaborar un breve resumen.

El aprendizaje basado en árboles de decisión utiliza un árbol de decisión como un modelo predictivo que mapea observaciones sobre un artículo a conclusiones sobre el valor objetivo del artículo. Es uno de los enfoques de modelado predictivo utilizadas en estadísticas, minería de datos y aprendizaje automático. Los modelos de árbol, donde la variable de destino puede tomar un conjunto finito de valores se denominan árboles de clasificación. En estas estructuras de árbol, las hojas representan etiquetas de clase y las ramas representan las conjunciones de características que conducen a esas etiquetas de clase. Los árboles de decisión, donde la variable de destino puede tomar valores continuos (por lo general números reales) se llaman **árboles de regresión**, es decir, que los árboles de regresión son el subtipo de árboles de decicon que se aplica cuando la variable respuesta es continua (real). 

En los modelos de regresión se intenta predecir el valor de una variable en función de otras variables que son independientes entre sí. Por ejemplo, queremos predecir el precio de venta del terreno en función de variables como su localización, superficie, distancia a la playa, etc. El posible resultado no forma parte de un conjunto predefinido, sino que puede tomar cualquier posible valor.

### Idea intuitiva

En términos generales, en el entrenamiento de un árbol de regresión, las observaciones se van distribuyendo por bifurcaciones (nodos) generando la estructura del árbol hasta alcanzar un nodo terminal. Cuando se quiere predecir una nueva observación, se recorre el árbol acorde al valor de sus predictores hasta alcanzar uno de los nodos terminales. La predicción del árbol es la media de la variable respuesta de las observaciones de entrenamiento que están en ese mismo nodo terminal.

### Arboles de Regressión vs. Arboles de Clasificación

![image](https://user-images.githubusercontent.com/88351747/139615056-c0772aac-7e0e-462e-a417-e7ecc2952cfd.png)

### Ejemplo

El set de datos Hitter contiene información sobre 322 jugadores de béisbol de la liga profesional. Entre las variables registradas para cada jugador se encuentran: el salario (Salary), años de experiencia (Years) y el número de bateos durante los últimos años (Hits). Utilizando estos datos, se quiere predecir el salario (en unidades logarítmicas) de un jugador en base a su experiencia y número de bateos. El árbol resultante se muestra en la siguiente imagen:

![image](https://user-images.githubusercontent.com/88351747/139616325-53ef0ed4-5896-4de1-9218-540853568369.png)

La interpretación del árbol se hace en sentido descendente. La primera división es la que separa a los jugadores en función de si superan o no los 4.5 años de experiencia. En la rama izquierda quedan aquellos con menos de 4.5 años, y su salario predicho se corresponde con el salario promedio de todos los jugadores de este grupo. La rama derecha se subdivide en función de si superan o no 117.5 bateos. Como resultado de las bifurcaciones, se han generado 3 regiones que pueden identificarse con la siguiente nomenclatura:

![image](https://user-images.githubusercontent.com/88351747/139616485-f1533a0e-deef-477c-8c70-1f31cbaacfe9.png)

A las regiones R1, R2 y R3 se les conoce como nodos terminales (terminal nodes o leaves), a los puntos en los que el espacio de los predictores sufre una división como nodos internos (internal nodes o splits) y a los segmentos que conectan dos nodos como ramas (branches).

La interpretación del modelo es: la variable más importante a la hora de determinar el salario de un jugador es el número de años jugados, los jugadores con más experiencia ganan más. Entre los jugadores con pocos años de experiencia, el número de bateos logrados en los años previos no tiene mucho impacto en el salario, sin embargo, sí lo tiene para jugadores con cuatro años y medio o más de experiencia. Para estos últimos, a mayor número de bateos logrados, mayor salario. Con este ejemplo queda patente que, la principal ventaja de los árboles de decisión frente a otros métodos de regresión, es su fácil interpretación y la gran utilidad de su representación gráfica.
