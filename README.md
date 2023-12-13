<h1 align="left"> Latin Squares </h1>

[![CL.png](https://i.postimg.cc/PrwWzzHz/CL.png)](https://postimg.cc/PPdvdDPP)
<h6> </h6>
<sub> Fig.1 </sub>
<h3></h3>
Índice

1. [Project description](#project-description)

2. [Project development](#Project-developmnet)

3. [Funcionalidad del proyecto](#funcionalidad-del-proyecto)

4. [Autores](#autores)

5. [Conclusión](#conclusión)


## Project description
<h4></h4>

The following project is about Latin squares, specifically delving into the orthogonality of these squares up to size n=6. We aim to verify that it is sufficient to find reduced Latin squares and that from these, we can determine the total number of Latin squares of size n. Additionally, we want our program to serve as a tool to confirm the non-existence of two mutually orthogonal Latin squares of order 6.

## Project development
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
Similar problems had been posed earlier, like Jacques Ozanam's French puzzle, placing kings, queens, jacks, and aces from a deck of cards in a 4x4 square so that each row and column contains each figure and suit exactly once.
<h6> </h6>
Euler solved various Latin squares, even of order greater than 6, but struggled with the 6x6 square, i.e., the 36 officers' problem. He conjectured that there is no solution when the order is an even number n ≡ 2 (mod 4) (recall 'being congruent': n ≡ 2 (mod 4) means n - 2 is a multiple of 4, i.e., n couldn't be 2, 6, 10, 14, 16, 22, …). In summary, the arrangement of n² officers with the described conditions was only possible when n is odd or a multiple of 4.
<h6></h6>
Both problems involve reconciling two conditions: army and rank in one, and card and suit in the other.
<h6></h6>
The two Latin squares forming a Greco-Latin square are said to be mutually orthogonal.
<h6></h6>

[![Imagen-2-580x167.png](https://i.postimg.cc/jStvXh3m/Imagen-2-580x167.png)](https://postimg.cc/HVvQWbg9)
<h6></h6>
<sub> Fig. 3 Example of 2 mutually orthogonal Latin squares </sub>

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
