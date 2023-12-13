<h1 align="left"> Latin Squares </h1>

[![CL.png](https://i.postimg.cc/PrwWzzHz/CL.png)](https://postimg.cc/PPdvdDPP)
<h6> </h6>
<sub> fig.1 </sub>
<h3></h3>
Índice

1. [Descripción del proyecto](#descripción-del-proyecto)

2. [Desarrollo del proyecto](#desarrollo-del-proyecto)

3. [Funcionalidad del proyecto](#funcionalidad-del-proyecto)

4. [Autores](#autores)

5. [Conclusión](#conclusión)


## Descripción del proyecto
<h4></h4>
El siguiente proyecto habla sobre los cuadrados latinos, mas especificamente, ahondaremos en la ortogonalidad de estos hasta los de tamaño n=6, queremos comprobar que basta con encontrar los cuadrados latinos reducidos y que a partir de estos podemos conocer el número completo de cuadrados latinos de tamaño n.
Además queremos que nuestro programa sea un apoyo para comprobar que no existen 2 cuadrados latinos mutuamente ortogonales de orden 6.


## Desarrollo del proyecto
<h4></h4>
<h3 align="left">¿Qué es un cuadrado latino?</h3>

[![xddd.jpg](https://i.postimg.cc/XqvbQDP7/xddd.jpg)](https://postimg.cc/62FgQzwD)
<h6> </h6>
<sub> fig.2 Cuadro del pintor suizo Richard Paul Lohse, que bajo el título “Komplementäre Gruppen durch sechs horizontale systematische Farbreihen” -Grupos complementarios formados por seis series sistemáticas horizontales de color- (1950 y 1976), recoge un cuadrado latino de orden 6 cuyos símbolos son los colores. </sub>
<h6> </h6>
<h6> </h6>
Un cuadrado latino de orden n es un retículo cuadrado de tamaño n x n en el que cada entrada es un número del 1 al n (el nombre de cuadrado latino viene de las letras del alfabeto latino que utilizó el matemático suizo Leonhard Euler), de tal forma que cada número de {1,…, n} aparece una vez, y sólo una vez, en cada fila y cada columna.
Si en la imagen anterior a cada color le asignamos un número tendremos ahora un cuadrado latino con la conjetura que deescribimos, o vease la fig. 1 para una mejor comprensión.
<h6> </h6>
<h3> El problema de los 36 oficiales y la conjetura de Euler </h3>
<h2></h2>
El problema de los 36 oficiales descrito por Leonhard Euler a finales del siglo XVIII; ¿es posible disponer a treinta y seis oficiales de seis regimientos distintos y de cada uno de los seis grados, en un cuadrado de 6x6 de forma que no coincidan dos oficiales del mismo rango o del mismo regimiento en ninguna fila y en ninguna columna?
<h6> </h6>
Problemas como este ya se habían planteado anteriormente como el de el frances Jacques Ozanam el cual plantea colocar los reyes, reinas, jotas y ases de una baraja de cartas, formando un cuadrado 4 x 4, tal que cada fila y cada columna contenga una vez y solo una vez, cada una de las figuras y cada uno de los palos.
<h6> </h6>
Euler pudo resolver varios cuadrados latinos incluso de orden mas grande que 6, pero fue incapaz de resolver el de 6 x 6, es decir, el de los 36 oficiales, así que se puso a pensar la situación en general, de modo que conjeturó que no existe solución cuando el orden es un número par n ≡ 2 (mod 4) (Recordemos lo que significa 'ser congruente': n ≡ 2 (mod 4), quiere decir que n – 2 es un múltiplo de 4, o sea n no podía ser 2, 6, 10, 14, 16, 22, …). En resumen, que la disposición de n² oficiales con las condiciones descritas sólo era posible cuando n fuera impar o múltiplo de 4.
<h6></h6>
En ambos problemas debemos compaginar dos condiciones. En uno el ejército y el rango, y en el otro, la carta y el palo al que pertenece.
<h6></h6>
Los dos cuadrados latinos que forman un cuadrado greco-latino se dice que son cuadrados latinos ortogonales.
<h6></h6>

[![Imagen-2-580x167.png](https://i.postimg.cc/jStvXh3m/Imagen-2-580x167.png)](https://postimg.cc/HVvQWbg9)
<h6></h6>
<sub> fig. 3 Ejemplo de 2 cuarados latinos mutuamente ortogonales </sub>

<h3 align="left"> Fundamentos matematicos </h3>
<h4>Definición: Ortogonal</h4>
<h6></h6>
Dos cuadrados latinos S1 y S2 son ortogonales si cuando miramos cada posición en turno y consideramos el par ordenado formado por la entrada de S1 en esa posición, y la entrada de S2 en esa posición, aparece cada par ordenado posible.
<h6></h6>
<h4>Definición: Mutuamente ortogonal</h4>
<h6></h6>
Un conjunto de cuadrados latinos es mutuamente ortogonal si cada par distinto de cuadrados latinos en el conjunto son ortogonales. Llamamos a tal conjunto, un conjunto de MOLS (para Cuadrados Latinos Mutuamente Ortogonales).
<h6></h6>
¿Cuántos cuadrados latinos puede haber en un conjunto de MOLS?, para tratar de resolver esta pregunta usaremos algunos resultados en los que nos apoyamos para la elaboración de nuestro proyecto.
<h6></h6>
<h3>Resultados<h/3>
<h6></h6>
<h4> Resultado 1 </h4>
Si S es un conjunto de MOLS de orden n, entonces |S|≤n−1.
<h4> Resultado 2</h4>
No existen 2 cuadrados latinos Mutuamente ortogonalda de orden 6
<h4>Resultado 3</h4>
Si un cuadrado latino es ortogonal a otro, las operaciones internas (permutacion entre filas o columnas), nos darán cómo resultado un cuadrado latino diferente que sigue conservando la ortogonalidad 



























## Funcionalidad del proyecto
°Generar cuadrados latinos de orden n≤6
°Encontrar cuadrados latinos mutuamente ortogonalds (MOLS) de orden 3≤n≤5
°Comprobar que no existen 2 cuadrados latinos mutuamente ortogonales de orden 6









## Autores
| [<img src="https://avatars.githubusercontent.com/u/141696762?v=4" width=115><br><sub>Cesar Augusto Zarco Moreno</sub>](https://github.com/CesarZarco) |  [<img src="https://avatars.githubusercontent.com/u/141844905?v=4" width=115><br><sub>Omar Samuel Pérez Pérez</sub>](https://github.com/OS37) |  [<img src="https://avatars.githubusercontent.com/u/141780211?v=4" width=115><br><sub>Juan Carlos Haro Ortega</sub>](https://github.com/jcar2905) |
| :---: | :---: | :---: |



## Conclusión
