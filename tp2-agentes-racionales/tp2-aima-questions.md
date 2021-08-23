# F) Responder preguntas 2.10 y 2.11 de AIMA 3era Edición.
### 2.10) Considere una versión modificada del entorno de vacío del ejercicio 2.8, en el que el agente recibe una penalización de un punto por cada movimiento.
**A) ¿Puede un simple agente reflexivo ser perfectamente racional para este entorno? Explicar.**

No puede un simple agente reflejo ser perfectamente racional para este entorno ya que estos agentes seleccionan las acciones en base a las percepciones actuales, ignorando percepciones históricas. Este agente aspiradora toma sus decisiones sólo con base en la localización actual y si ésta está sucia por lo que no puede optimizar la cantidad de movimientos porque no tiene una percepción de como es el ambiente totalmente, puede seguir patrones para ser un poco más eficiente pero no lograra maximizar la medida de rendimiento todo lo posible.

**B) ¿Qué pasa con un agente reflexivo con el estado?** 

En este caso si podría ser racional ya que el estado está dado por experiencias anteriores (registro) y se tiene un conocimiento. 

**C) ¿Cómo cambian sus respuestas a y b si las percepciones del agente le dan el estado limpio / sucio de cada cuadrado del entorno?**

En la situación a, seria racional ya que este buscaria las posiciones sucias. En la situacion b, no cambiaria nada.

### 2.11) Considere una versión modificada del entorno de vacío del ejercicio 2.8, en el que se desconoce la geografía del entorno —su extensión, límites y obstáculos—, al igual que la configuración inicial del suelo. (El agente puede ir hacia arriba y hacia abajo, así como hacia la izquierda y hacia la derecha).

**A) ¿Puede un simple agente reflexivo ser perfectamente racional para este entorno? Explicar.**

No, como en el caso anterior, el agente no puede optimizar la cantidad de movimientos porque no tiene una percepción de como es el ambiente, solo de su estado actual.

**B) ¿Puede un agente reflejo simple con una función de agente aleatoria superar a un agente reflejo simple?**

No, como se vio en el ejercicio tp2-results.md. Tiene mejores resultados el Agente Reflexivo Simple.

**C) ¿Puede diseñar un entorno en el que su agente asignado al azar tenga un desempeño deficiente? Muestre sus resultados.**

Para un entorno de 128x128 con porcentaje de suciedad de 0.8 (1639 casillas sucias) solo se limpian 9 casillas teniendo solo 9 puntos cuando lo eficiente seria por lo menos acercarse a los 500 puntos de rendimiento, con rendimiento que no sea al azar (en el caso de que la vida solo permita realizar 1000 acciones.) 

**D) ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple?**

Si lo puede superar ya que tienen una percepción más completa del entorno gracias a los estados y esto hace que tengan mejor conocimiento y puedan maximizar las acciones ya que estas están tomadas en base a lo que se sabe.
