# INTELIGENCIA ARTIFICIAL: FUNDAMENTOS FILOSÓFICOS
Los filosos definen la hipótesis de la **IA débil** como la afirmación de que es posible que las máquinas actúen como si fueran inteligentes; y la hipótesis de la **IA fuerte** es la afirmación de que las máquinas piensan realmente.
La mayoría de los investigadores de IA dan por sentado la IA débil, y no se preocupan por la fuerte, con tal de que funcione su programa no interesa si se llama simulación o inteligencia real. 

![image](https://user-images.githubusercontent.com/88351747/129025548-ebc56e6d-98ff-44ce-9ae0-1b0136450dfe.png)


## IA DÉBIL
Los filósofos están interesados en comparar dos arquitecturas, la humana y la máquina. Además, han formulado la pregunta:  *¿Pueden pensar las máquinas?*. Esta cuestión no está bien definida. 
Turing sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si pueden aprobar un test de inteligencia conductiva (***Test de Turing***) donde el programa mantiene una conversación durante cinco minutos (online) con un interrogador que debe averiguar si la conversación se está llevando a cabo con un programa o una persona; si el programa engaña al interlocutor un 30% del tiempo, pasa la prueba. Algunas personas han sido engañadas, sin embargo, ningún programa se ha acercado al criterio frente a jueces con conocimiento, y el campo de la IA no ha prestado mucha atención al test.
Turing examinó objeciones ante la posibilidad de las máquinas inteligentes:

### 1.	Argumento de la incapacidad 
Afirma que ***una maquina nunca puede hacer X:***
> Ser amable, tener recursos, ser guapo, simpático, tener iniciativas, tener sentido del humor, distinguir lo correcto de lo erróneo, cometer errores, enamorarse, disfrutar con las fresas con nata, hacer que otra persona también se enamore, aprender de la experiencia, utilizar palabras de forma adecuada, ser el tema de su propio pensamiento, tener tanta diversidad de comportamientos como el hombre, hacer algo realmente nuevo. 

Pero actualmente los computadores juegan ajedrez, comprueban ortografía, conducen, diagnostican enfermedades, y hacen descubrimientos. Además a veces funcionan en tareas que se relacionan con el juicio humano. Paul Meehl estudió los procesos de la toma de decisiones de expertos en tareas como predecir el éxito de un alumno en un programa de formación, o la reincidencia de un delincuente, y además desde 1999 Educational Testing Service ha utilizado un programa automatizado para calificar preguntas de redacciones en el examen GMAT, que concuerda con los examinadores en un 97% (mismo nivel de concordancia entre dos personas).
Los computadores pueden hacer muchas cosas *tan bien o mejor que el humano*. Pero esto no significa que utilicen la intuición y el entendimiento. También es cierto que existen tareas en donde no sobresalen, como mantener una conversación abierta.

### 2.	Objeción matemática: 
Ciertas cuestiones matemáticas no pueden ser respondidas por sistemas formales. El teorema de la incompletitud de Gödel un ejemplo. 
Filósofos han afirmado que: este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, porque son sistemas formales limitados por el teorema de la incompletitud, es decir no pueden establecer la verdad de su propia sentencia Gödel, mientras que los hombres sí. 
Podemos ver problemas en esta afirmación. El teorema se aplica sólo a sistemas formales potentes como para realizar aritmética. Además un agente no debería avergonzarse de no poder establecer la verdad de una sentencia aunque otros sí puedan y aunque reconozcamos que los computadores tienen limitaciones, no existen evidencias de que los hombres sean inmunes ante estas. Es sencillo demostrar que un sistema formal no puede hacer X, y afirmar que los hombres pueden hacerlo, sin dar evidencia. Sin embargo se sabe que los hombres son inconsistentes para el razonamiento diario, pero también es verdadero para un pensamiento matemático. 

### 3.	Argumento de la informalidad
Consiste en que el ***comportamiento humano es demasiado complejo para captarse mediante reglas*** y como los computadores hacen más que seguir reglas, no pueden generar un comportamiento tan inteligente como el del hombre. En IA la incapacidad de capturarlo todo en un conjunto de reglas lógicas se denomina **problema de cualificación** 
El filósofo que ha propuesto principalmente este punto de vista ha sido Dreyfus. Junto con su hermano proponen una arquitectura de redes neurales organizadas, pero señalan algunos problemas: 
-	No se puede lograr una generalización buena de ejemplos sin un conocimiento básico. Afirman que no se sabe cómo incorporar el conocimiento básico en el proceso de aprendizaje de las redes neuronales. Pero esta también es una buena razón para realizar un rediseño serio de los modelos actuales del procesamiento neuronal de forma que puedan sacar provecho del conocimiento aprendido anteriormente como lo hacen otros algoritmos de aprendizaje. 
-	El aprendizaje de redes neuronales es una forma de aprendizaje supervisado que requiere la identificación de las entradas relevantes y las salidas correctas. Por tanto, afirman que no puede funcionar autónomamente sin la ayuda de un entrenador humano.
-	Los algoritmos de aprendizaje no funcionan bien con muchas funciones, si seleccionamos un subgrupo de éstas, «no existe una forma conocida de añadir funciones nuevas, si el conjunto actual demuestra ser inadecuado para tener en cuenta los hechos aprendidos». 
-	El cerebro es capaz de dirigir sus sensores para buscar la información relevante y procesarla para extraer aspectos relevantes para la situación actual. Sin embargo, afirman que «Actualmente, los detalles de este mecanismo ni se entienden y ni siquiera se hipotetizan para guiar la investigación en la IA». 

Muchos temas tratados por Dreyfus se han incorporado en el diseño estándar de agentes inteligentes. Esta es una evidencia del progreso de la IA, y no de su imposibilidad. 

## IA FUERTE
Muchos filósofos afirman que una máquina que pasa el Test de Turing no quiere decir que esté realmente pensando, sería solo una ***simulación*** de la acción. Esta objeción fue prevista por Turing, y cita: 
> Hasta que una máquina pueda escribir un soneto o componer un concierto porque sienta los pensamientos y las emociones, y no porque haya una lluvia de símbolos, podría reconocer que la máquina iguala al cerebro, es decir, no sólo escribirlo sino que sepa que lo ha hecho. 

Esto es lo que llama el argumento de la **consciencia**, la máquina tiene que ser consciente de sus acciones y estados mentales. El punto de vista clave se relaciona con la **fenomenología** de la experiencia directa, es decir, la máquina tiene que sentir emociones. Otros se centran en la **intencionalidad**, que es la cuestión de si las creencias, deseos y otras representaciones de la máquina son de verdad algo que pertenece al mundo real. 

Turing niega que la conciencia sea relevante para la IA. Interesa crear programas que se comporten de forma inteligente y no si alguien los declara reales o simulados. Por muchos filósofos están interesados en esta cuestión. 
Cuando se sintetizó urea artificial, los químicos reconocieron que era urea porque tenía las propiedades adecuadas. Igualmente, el edulcorante artificial es edulcorantes. Por otro lado, las flores artificiales no son flores, ni tampoco un Picasso artificial sería un Picasso. . Entonces nos podemos preguntar ¿Son los procesos mentales parecidos al Picasso..., o a la urea? En cada caso parece ser una cuestión de convención. Sin embargo para las mentes artificiales, no existe una convención. Todo depende de la teoría de los estados y los procesos mentales.

La ***teoría del funcionalismo*** dice que un estado mental es cualquier condición causal inmediata entre la entrada y la salida. Dos sistemas con procesos causales isomórficos tendrían los mismos estados mentales. Por tanto, un programa informático podría tener los mismos estados mentales que una persona.

En contraste, la ***teoría del naturalismo biológico*** dice que los estados mentales son características emergentes de alto nivel originadas por procesos neurológicos de bajo nivel en las neuronas, y lo que importa son las propiedades de las neuronas. Así pues, los estados mentales no se pueden duplicar en la base de algún programa; necesitaríamos que el programa se ejecutara en una arquitectura con la misma potencia causal que las neuronas.

Para investigar estos dos puntos de vista examinaremos un problema antiguo de la filosofía, y tres experimentos. 

### El problema de mente-cuerpo
Cuestiona cómo se relacionan los estados y procesos mentales con los estados y los procesos (específicamente del cerebro) del cuerpo, lo generalizamos como un problema de *«arquitectura-mente*, para que nos permita hablar sobre la posibilidad de que las máquinas tengan mentes. 

Para la primera dificultad nos remontaremos a Descartes, quien abordó que un alma inmortal interactúa con un cuerpo mortal, y concluyó que el alma y el cuerpo son dos tipos de cosas diferentes, una teoría **dualista**. 

La teoría monista, o **materialismo**, mantiene que no existen almas inmateriales, sino sólo objetos materiales. Como consecuencia, los estados mentales (sentir dolor, saber que alguien está montando a caballo) son estados del cerebro. 
El materialista se debe enfrentar con dos obstáculos. El primero es la libertad de elección: ¿Cómo una mente puramente física conserva el libre albedrío? La mayoría de los filósofos consideran que este problema necesita una reconstitución de noción de libertad de elección. El segundo problema tiene que ver con la conciencia, el por qué se siente algo cuando se tienen ciertos estados cerebrales, mientras que probablemente no se siente nada al tener otros estados físicos. 

Para empezar a responder estas cuestiones, necesitamos formas de hablar sobre los estados del cerebro a niveles más abstractos que las configuraciones específicas los átomos del cerebro. Vamos a examinar una clase en particular de estado mental: las **actitudes proposicionales**, o estados intencionales (creer, desear, temer, y otros que se relacionan con algunos aspectos del mundo exterior). Estos estados tienen una conexión con objetos del mundo externo. Por otro lado se ha argumentado que los estados mentales son estados del cerebro, y de aquí que los estados mentales de identidad o no-identidad se deberían determinar permaneciendo completamente «dentro de la cabeza», sin hacer referencia al mundo real. Para examinar este dilema retomaremos el experimento del pensamiento que intenta separar a los estados intencionales de sus objetos externos. 

### El experimento del «cerebro en una cubeta» 
Imagínese que al nacer le extraen el cerebro y lo colocan en una cubeta que lo mantiene y le permite desarrollarse. Al mismo tiempo recibe señales de un simulador que de un mundo ficticio. A continuación, el estado del cerebro podría tener el estado mental MueroPor (Yo, Hamburguesa) aunque no tenga un cuerpo con el que sentir hambre. En ese caso, ¿sería el mismo estado mental que el del cerebro en un cuerpo? 

Una forma de resolver esto es decir que el contenido de los estados mentales puede ser interpretado desde dos puntos de vista. La visión del **contenido extenso** interpreta el dilema desde el punto de vista de un observador omnisciente desde fuera con acceso a la situación completa, y puede distinguir las diferencias del mundo. De esta manera las ideas del cerebro en una cubeta son diferentes de las de una persona. El **contenido estrecho** sólo tiene en cuenta el punto de vista subjetivo interno, y bajo este punto de vista todas las creencias serían las mismas. 

Ahora vamos a entrar en la esfera de **qualia** («tales cosas»). Suponga que una persona X experimenta en rojo el color que Y percibe como verde, y viceversa. Entonces cuando ambas vean el semáforo actuarán de la misma manera, pero la experiencia que tienen será diferente. No está claro si eso significa que son los mismos estados mentales o diferentes. 
Ahora vemos otro experimento que aborda la cuestión de si los objetos físicos diferentes a las neuronas humanas pueden tener estados mentales. 

### El experimento de la prótesis cerebral 
Consiste en sustituir gradualmente las neuronas de la cabeza de alguien y a continuación invertir el proceso para retornar al sujeto a su estado biológico normal. 
Por definición del experimento, él comportamiento externo del sujeto no debe sufrir cambios. Existe una confrontación de intuiciones de lo que podría llegar a ocurrir. Moravec, está convencido de que su consciencia no se vería afectada y Searle está convencido de que esta desaparecería.
Patricia Churchland señala que los argumentos funcionalistas que operan a nivel de neurona también pueden funcionar al nivel de cualquier unidad funcional más grande, un grupo de neuronas, un módulo mental, un lóbulo, o todo el cerebro. Eso significa que si la noción de que el experimento muestra que el cerebro de sustitución es consciente, deberíamos también creer que la consciencia se mantiene cuando el cerebro entero se sustituye por un circuito que hace corresponder la entrada con la salida mediante una tabla de búsqueda. 

### La habitación china 
Describe un sistema hipotético que está ejecutando un programa y que pasa la prueba de Turing, pero que no entiende ninguna entrada ni salida. La conclusión es que ***ejecutar el programa adecuado no es condición suficiente para ser una mente***. 
El sistema se compone de un hombre, que solo entiende inglés, con un libro de reglas y pilas de papel, algunas en blanco y otras con inscripciones indescifrables. El sistema se encuentra dentro de una habitación con apertura al exterior. A través de la apertura se van deslizando los papeles con símbolos. El hombre encuentra los símbolos correspondientes en el libro de reglas y sigue las instrucciones. Finalmente los símbolos serán transcritos y se pasan al mundo exterior. 

El objetivo del argumento de la habitación china es refutar la IA fuerte, es decir la afirmación de que ejecutar la clase adecuada de programa da como resultado necesariamente una mente. Apela a la intuición: ¿qué hay en la habitación que sea una mente? Sin embargo, se podría hacer el mismo argumento sobre el cerebro: observe el conjunto de células que funcionan según las leyes de la Bioquímica: ¿Qué hay ahí que sea una mente? ¿Por qué un trozo de cerebro puede ser una mente mientras que uno de hígado no? 

## LA ÉTICA Y LOS RIESGOS DE DESARROLLAR LA INTELIGENCIA ARTIFICIAL 
Quienes desarrollan IA se enfrentan a consideraciones éticas. Se exponen problemas nuevos:

-	**Las personas podrían perder sus trabajos por la automatización.** 
La economía depende de los computadores. Miles de trabajadores han sido desplazados por la IA, pero en contraposición la automatización por la IA ha creado más trabajos de los que ha eliminado, y son más interesantes y mejor pagados. 

-	**Las personas podrían tener demasiado (o muy poco) tiempo de ocio.**
Aunque en realidad, en una economía de la información existe una gran recompensa por ser ligeramente mejor que la competencia; trabajar un 10% más podría significar un 100 por 100 de incremento en los ingresos. La IA incrementa el ritmo de la innovación tecnológica y contribuye así a esta tendencia general, pero también mantiene la promesa de permitirnos ahorrar tiempo y que nuestros agentes automatizados hagan las cosas por un tiempo. 

-	**Las personas podrían perder el sentido de ser únicos.** 
Weizenbaum argumenta que la investigación en IA hace posible la idea de que los hombres sean autómatas, es decir con pérdida de autonomía o de humanidad. La IA, aunque sea una materia de gran éxito, quizá sea por lo menos amenazante para las suposiciones morales de la sociedad del siglo XXI al igual que la teoría de la evolución lo fue para los del siglo XIX. 

-	**Las personas podrían perder algunos derechos privados.** 
Algunas personas reconocen que la computarización conduce a la pérdida de privacidad, aunque algunos piensan que de cualquier forma tenemos privacidad cero, otros no están de acuerdo y afirman que la privacidad es un derecho que debe tenerse en cuenta.

-	**La utilización de los sistemas de IA podría llevar a la pérdida de responsabilidad.** 
En algunas circunstancias se puede culpar a los agentes de la IA por decisiones poco razonables o equivocada, para esto hay que tener en cuenta que son herramientas de las cuales los verdaderos responsables son quienes las utilizan y las crean, aunque esto podría desvirtuarse. Además, la ley tiene todavía que ponerse a la altura de los nuevos desarrollos. 

-	**El éxito de la IA podría significar el fin de la raza humana.** 
Cualquier tecnología tiene potencial de hacer daño si se encuentra en las manos equivocadas, pero con la IA las manos equivocadas podrían pertenecer a dicha tecnología.
Una máquina ultrainteligente podría diseñar máquinas incluso mejores; entonces existiría una «explosión de inteligencia», y la inteligencia del hombre quedaría atrás. La «explosión de inteligencia» ha sido llamada singularidad tecnológica. 

Hans Moravec predice que los robots se igualarán a la inteligencia humana en 50 años y a continuación la excederán: 
>“De manera bastante rápida podríamos quedar desplazados y fuera de la existencia. No estoy tan alarmado como muchos otros por esta última posibilidad, ya que considero que las máquinas del futuro son nuestra progenie, «hijos de mente» construidos a nuestra imagen y semejanza, es decir, nosotros mismos pero en una forma más potente. Al igual que los hijos biológicos de generaciones anteriores, representarán la mejor esperanza de la humanidad para un futuro a largo plazo. Nos corresponde a nosotros ofrecerles todas las ventajas, y cómo retirarnos cuando ya no podamos contribuir”>

Ray Kurzweil predice que en 2099 existirá «una fuerte tendencia hacia una fusión del pensamiento humano en el mundo de la inteligencia de la máquina que las especies humanas crearon inicialmente. Ya no existe una distinción entre hombres y computadores». Es el trashumanismo. 

## OPINION PERSONAL
Opino que al crear IA se debe buscar cumplir el término de IA débil y dejar un poco de lado la IA fuerte ya que me parece que mientras se cumplan los objetivos prácticos de manera eficiente, realmente no importa si lo que se está usando para resolver las necesidades es una forma de pensamiento real como el de los humanos.
Al final ¿de que nos sirve buscar la similitud humana? Si ya, sin responder estos dilemas y preguntas sobre la consciencia y los estados mentales, se ha logrado replicar y mejorar las actividades que antes realizaba solo una persona. Lo importante es enfocarse en optimizar los sistemas. 

Todo esto, siempre y cuando se tenga en cuenta las cuestiones éticas y morales correspondientes. El criterio para crear IA debe ser muy importante y evaluarse en cada momento. Ya que si no tenemos las precauciones podemos encontrar amenazas hacia nuestra especie. Los robots deben actuar moralmente, programarlos con una teoría de lo que está bien y lo que no y, a su vez, las personas capacitadas en la creación de estas tecnologías deben cumplir criterios éticos y debe haber una regulación estricta.

Las personas deben tomar responsabilidad, creo que la IA es una herramienta y no debe utilizarse como un reemplazo definitivo de algunas acciones. No se debe perder el objetivo principal (optimizar) dejando que el ocio, la desinformación y la violación de derechos opaquen las cosas maravillosas que se pueden realizar con esta tecnología.

A continuación dejo un [ mapa][ m ] mental como sintesis del texto.

[ m]: https://www.mindomo.com/mindmap/1dc27d47b128485b9d717735c44a1045
