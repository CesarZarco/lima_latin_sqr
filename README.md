<h1 align="left"> Latin Squares </h1>

[![CL.png](https://i.postimg.cc/PrwWzzHz/CL.png)](https://postimg.cc/PPdvdDPP)
<h6> </h6>
<sub> Fig.1 </sub>
<h3></h3>
Índice

1. [Project description](#project-description)

2. [Project development](#project-developmnet)

3. [Project Functionality](#project-functionality)

4. [Autors](#autors)

5. [Conclusion](#conclusion)


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

<h3 align="left"> Mathematical Foundations </h3>
<h4> Definition: Orthogonal </h4>
<h6></h6>
Two Latin squares S1 and S2 are orthogonal if, when we look at each position in turn and consider the ordered pair formed by the entry of S1 in that position and the entry of S2 in that position, every possible ordered pair appears.
<h6></h6>
<h4> Definition: Mutually Orthogonal </h4>
<h6></h6>
A set of Latin squares is mutually orthogonal if every distinct pair of Latin squares in the set is orthogonal. We call such a set a set of MOLS (Mutually Orthogonal Latin Squares).
<h6></h6>
How many Latin squares can exist in a set of MOLS? To try to answer this question, we will use some results that we rely on for the development of our project.
<h6></h6>
<h3>Results<h/3>
<h6></h6>
<h4> Result 1 </h4>
If S is a set of MOLS of order n, then |S| ≤ n−1.
<h4> Result 2</h4>
There do not exist 2 mutually orthogonal Latin squares of order 6.
<h4>Result 3</h4>
If one Latin square is orthogonal to another, internal operations (permutation between rows or columns) will result in a different Latin square that still maintains orthogonality.

























## Project functionality
- Generate Latin squares of order n≤6.
- Find mutually orthogonal Latin squares (MOLS) of order 3≤n≤5.
- Verify the non-existence of 2 mutually orthogonal Latin squares of order 6.








##Autors
| [<img src="https://avatars.githubusercontent.com/u/141696762?v=4" width=115><br><sub>Cesar Augusto Zarco Moreno</sub>](https://github.com/CesarZarco) |  [<img src="https://avatars.githubusercontent.com/u/141844905?v=4" width=115><br><sub>Omar Samuel Pérez Pérez</sub>](https://github.com/OS37) |  [<img src="https://avatars.githubusercontent.com/u/141780211?v=4" width=115><br><sub>Juan Carlos Haro Ortega</sub>](https://github.com/jcar2905) |
| :---: | :---: | :---: |



## Conclusion
