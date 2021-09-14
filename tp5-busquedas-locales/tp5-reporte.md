# Parte II
## A) Ejecutar cada uno de los algoritmos implementados en la parte I 30 veces y calcular para el caso de 4, 8, 10,12 y 15 reinas:
### 1. El número (porcentaje) de veces que se llega a un estado de solución óptimo.

**Hill Climbing :** 44%, 13%, 7%, 0%, 0%

**Simulated Annealing:** 100%, 67%, 50%, 34%, 17%

**Algoritmo Genetico:** 100%, 94%, 67%, 50%, 27%


### 2. El tiempo de ejecución promedio y la desviación estándar para encontrar dicha solución.
<table class="default">
  <colgroup bgcolor="#555555">
  <colgroup span="2" bgcolor="#444444">
  <colgroup span="2" bgcolor="#555555">
  <colgroup span="2" bgcolor="#444444">
  <colgroup span="2" bgcolor="#555555">
  <tr bgcolor="#444444">
    <td></td>
    <td colspan="12" align="center">Tiempo de Ejecucion</td>
  </tr>
  <tr bgcolor="#666666">
    <td></td>
    <td colspan="2" align="center" >Hill Climbing</td>
    <td colspan="2" align="center" >Simulated Annealing</td>
    <td colspan="2" align="center" >Algoritmo Genetico</td>
  </tr>
  <tr >
    <th>Tamaño</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
  </tr>
  <tr>
    <td align="center">4x4</td>
    <td align="center">0</td>
    <td align="center">0</td>
    <td align="center">0,333</td>
    <td align="center">0,018</td>
    <td align="center">0,03</td>
    <td align="center">0,047</td>
  </tr>
  <tr>
    <td align="center">8x8</td>
    <td align="center">0,02</td>
    <td align="center">0,041</td>
    <td align="center">0,04</td>
    <td align="center">0,049</td>
    <td align="center">0,183</td>
    <td align="center">0,046</td>
  </tr>
  <tr>
    <td align="center">10x10</td>
    <td align="center">0,056</td>
    <td align="center">0,050</td>
    <td align="center">0,073</td>
    <td align="center">0,052</td>
    <td align="center">0,35</td>
    <td align="center">0,057</td>
  </tr>
  <tr>
    <td align="center">12x12</td>
    <td align="center">0,156</td>
    <td align="center">0,051</td>
    <td align="center">0,103</td>
    <td align="center">0,050</td>
    <td align="center">0,57</td>
    <td align="center">0,108</td>
  </tr>
  <tr>
    <td align="center">15x15</td>
    <td align="center">0,446</td>
    <td align="center">0,074</td>
    <td align="center">0,21</td>
    <td align="center">0,759</td>
    <td align="center">1,27</td>
    <td align="center">0,293</td>
  </tr>
</table>
    
### 3. La cantidad de estados previos promedio y su desviación estándar por los que tuvo que pasar para llegar a una solución.

<table class="default">
  <colgroup bgcolor="#555555">
  <colgroup span="2" bgcolor="#444444">
  <colgroup span="2" bgcolor="#555555">
  <colgroup span="2" bgcolor="#444444">
  <colgroup span="2" bgcolor="#555555">
  <tr bgcolor="#444444">
    <td></td>
    <td colspan="12" align="center">Estados Previos</td>
  </tr>
  <tr bgcolor="#666666">
    <td></td>
    <td colspan="2" align="center" >Hill Climbing</td>
    <td colspan="2" align="center" >Simulated Annealing</td>
    <td colspan="2" align="center" >Algoritmo Genetico</td>
  </tr>
  <tr >
    <th>Tamaño</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
    <th>Media Aritmetica</th>
    <th>Desviacion Estandar</th>
  </tr>
  <tr>
    <td align="center">4x4</td>
    <td align="center">1,466</td>
    <td align="center">1,042</td>
    <td align="center">23,066</td>
    <td align="center">14,154</td>
    <td align="center">6</td>
    <td align="center">1,15</td>
  </tr>
  <tr>
    <td align="center">8x8</td>
    <td align="center">3,4</td>
    <td align="center">0,932</td>
    <td align="center">188,16,</td>
    <td align="center">250</td>
    <td align="center">77</td>
    <td align="center">63</td>
  </tr>
  <tr>
    <td align="center">10x10</td>
    <td align="center">4,033</td>
    <td align="center">1,067</td>
    <td align="center">316</td>
    <td align="center">294</td>
    <td align="center">549</td>
    <td align="center">372</td>
  </tr>
  <tr>
    <td align="center">12x12</td>
    <td align="center">4,9</td>
    <td align="center">0,959</td>
    <td align="center">294</td>
    <td align="center">212</td>
    <td align="center">883</td>
    <td align="center">287</td>
  </tr>
  <tr>
    <td align="center">15x15</td>
    <td align="center">6,1</td>
    <td align="center">1,155</td>
    <td align="center">334</td>
    <td align="center">201</td>
    <td align="center">898</td>
    <td align="center">294</td>
  </tr>
</table>    
   
### 4. Generar un tabla con los resultados para cada uno de los algoritmos desarrollados y guardarla en formato .csv (comma separated value)
    
[Parte 2.xlsx](https://github.com/LuciaCairo/ia-uncuyo-2021-/files/7159095/Parte.2.xlsx)
    
## B) Para cada uno de los algoritmos, graficar la variación de la función h() a lo largo de las iteraciones.

![image](https://user-images.githubusercontent.com/88351747/133198965-4eeec34d-56e8-440a-91ad-71aeaad93428.png)

![image](https://user-images.githubusercontent.com/88351747/133198982-a6b9910a-53ec-4ccd-b665-e4375b872885.png)

![image](https://user-images.githubusercontent.com/88351747/133199012-aa39ea11-122c-404d-bb80-a87aa195228e.png)
    
## C) Indicar según su criterio, cuál de los tres algoritmos implementados resulta más adecuado para la solución del problema de las n-reinas. Justificar    
El algoritmo de Simulate es el mejor en este caso ya que alcanza la solucion optima la mayoria de las veces con una cantidad de estados previos aceptable, no podemos decir lo mismo del algoritmo genetico ya que este recorre muchos mas estados y varia mucho dependiendo de la poblacion inicial y demora mucho mas en ejecutarse; el hill climbing es tambien una buena opcion por que ejecuta muchos menos estados que los algoritmo mencionados anteriormente, pero tiene el prblema de que muy pocas veces encuentra la solucion optima ya que se queda en un optimo local y de alli es dificil salir, por lo que suele llegar a soluciones buenas pero no optimas.  
    
