<h1 align="left"> Latin Squares </h1>

[![CL.png](https://i.postimg.cc/PrwWzzHz/CL.png)](https://postimg.cc/PPdvdDPP)
<h6> </h6>
<sub> fig.1 </sub>
<h3></h3>
Índice

1. [Project description](#project-description)

2. [Desarrollo del proyecto](#desarrollo-del-proyecto)

3. [Funcionalidad del proyecto](#funcionalidad-del-proyecto)

4. [Autores](#autores)

5. [Conclusión](#conclusión)


## Project description
<h4></h4>

The following project is about Latin squares, specifically delving into the orthogonality of these squares up to size n=6. We aim to verify that it is sufficient to find reduced Latin squares and that from these, we can determine the total number of Latin squares of size n. Additionally, we want our program to serve as a tool to confirm the non-existence of two mutually orthogonal Latin squares of order 6.

## Desarrollo del proyecto
<h4></h4>
<h3 align="left"> What is a Latin Square?</h3>

[![xddd.jpg](https://i.postimg.cc/XqvbQDP7/xddd.jpg)](https://postimg.cc/62FgQzwD)
<h6> </h6>
<sub> Fig. 2 Square by Swiss painter Richard Paul Lohse, titled "Komplementäre Gruppen durch sechs horizontale systematische Farbreihen" - Complementary groups formed by six horizontal systematic color series - (1950 and 1976), displays a Latin square of order 6 where symbols are colors.  </sub>
<h6> </h6>
<h6> </h6>
A Latin square of order n is an n x n square grid where each entry is a number from 1 to n (named Latin square due to the Latin alphabet letters used by Swiss mathematician Leonhard Euler). Each number from {1,...,n} appears exactly once in each row and each column.
If we assign a number to each color in the previous image, we will now have a Latin square with the conjecture we described, or see fig. 1 for a better understanding.
<h6> </h6>
<h3> The problem of the 36 officers and Euler's conjecture </h3>
<h2></h2>
The problem of the 36 officers described by Leonhard Euler in the late 18th century: Can thirty-six officers from six different regiments and each of the six ranks be arranged in a 6x6 square so that no two officers of the same rank or regiment coincide in any row or column?
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
