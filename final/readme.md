@author Yuting Su(suy@carleton.edu)
@author Starr Wang(wangy3@carleton.edu)

1.Description:
Modified from the classical candy crash game, Animal Crush is a match-three puzzle video game. In the game, player completes levels by swipping pieces of different animals on the game board to make a match of three or more of the same animal. As a result, the matching animals would be eliminated from the board and replaced by new ones. 

2.Why MVC is appropriate?
MVC is appropriate for our project because it helps to organize the projects in different parts. This is useful because it makes development process faster, as one person can work on view while the other can work on model. Also the modification of view will not affect the entire model, which is useful to update the program. 
For our Animal Crush game, the view is consisted of a game board and a score at the top. The model is consisted of two main classes: gameboard and grid. 

3.A list of the core classes that make up your Model.

class Gameboard: 
--this class represents the whole gameboard, which is used to keep track of the score, number of grids, and update the game board when the animal grids crushes.

--class variable: score, grids, gameOver

--class method: gameStart(), gameOver(), checkCrush(), swapGrid(), updateGameBoard(), updateScore(), update()


class Grid:
--this class represents one specific animal grid, which is used to identify the type of animal grids and keep track of the position.  

--class variable: position, animalType 

--class method: getPosition(), getAnimalType(), initializeAnimalType()

subclass of Lion, Deer, Dog, Cat


Plan
1.Create a random view at the beginning of the game
--Make subclass of each animal, return number 
--make a random view at the beginning of the game 



2.get response when users clicks two grids
3.swap the grids 
4.replace the grids with new grids and update score
5.deterimine when the game ends and update the view
6.replace grid with animal pictures 