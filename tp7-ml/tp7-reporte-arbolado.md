### A. Descripción del proceso de preprocesamiento (si es que lo hubiera)

Eliminé columnas que no aportaban información importante, como la última modificación, longitud, latitud , el área de la sección, y el nombre de la sección.
También busqué la clase mayoritaria, la cual es cuando los datos tienen inclinacion peligrosa = 0, y eliminé algunas filas. </h5>

### B. Resultados obtenidos sobre el conjunto de validación

**Matriz de confusion**

| | 0 | 1 |
| --------- | --------- | --------- |
| 0 | 2401 | 1178 |
| 1 | 925 | 1906 |

**Metricas**

| Accuracy| Precision | Sensitivity | Specificity |
| ------------- | ------------- | ------------- | ------------- |
| 0.8658728  | 0.8830981 | 0.9774583 | 0.02540107  |

### C. Resultados obtenidos en Kaggle

0.68083 </h5>

### D. Descripción detallada del algoritmo propuesto

Tomamos el conjunto data_set para entrenar y  a partir de el, predecir la inclinaicon peligrosa de los datos del data_test. Basandonos en la parte A del trabajo practico, eliminamos las columnas que nos parecian innecesarias (última modificación, longitud, latitud , área de la sección, nombre de la sección), dejando las realmente importantes como la seccion, la especie, el diametro del tronoco y la circunferencia del tronco, ya que vimos que algunas de estas variables definian la tendencia a tener una inclinacion peligrosa.  

Probamos usar variables categoricas en el diametro del tronco, pero vimos que esto no mejoraba los resultados, asi que no lo aplicamos.  
Balanceamos la clase mayoritaria, ya que observamos que esta tenia un porcentaje demasiado alto de arboles sin inclinacion peligrosa, quedando asi la misma cantidad de arboles con inclinacion peligrosa y no peligrosa.

Elegimos entrenar el conjunto data_set con Random Forest, ya que nos parecio bueno para generalizar, este algoritmo es una combinación de árboles predictores tal que cada árbol depende de los valores de un vector aleatorio probado independientemente y con la misma distribución para cada uno de estos. Finalmente con la funcion predict, estimamos la inclinacion peligrosa del conjunto de datos data_test.
