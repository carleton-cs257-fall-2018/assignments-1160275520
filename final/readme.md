@author Yuting Su(suy@carleton.edu)
@author Starr Wang(wangy3@carleton.edu)

1.Description:

![alt text](https://s3.amazonaws.com/backgroundpicture/animalcrush.png)

Modified from the classic candy crash game, Animal Crush is a video game to find matching animals. In the game, the player wants to find matching animals by swapping animal grids.

Every time the an animal grid is swapped to a new position, the algorithm will search nearby animal grids vertically and horizontally on the game board. If the nearby animals are the same as the swapped animal, they will crush with the swapped animal and replaced by new ones, and the player will get points.
 
The total points are equal to the total number of crushing animals. When the player reaches the target score, the game is reset to the next level.

2.Why MVC is appropriate?

MVC is appropriate for our project because it helps to organize the projects in different parts. This is useful because it makes development process faster, as one person can work on view while the other can work on model. Also the modification of view will not affect the entire model, which is useful to update the program. 
For our Animal Crush game, the view is consisted of a game board and a score at the top. The model is consisted of two main classes: GameBoardModel and AnimalModel. 

3.A list of the core classes that make up your Model.

class GameBoardModel: 

--this class represents the whole game board, which is used to keep track of the score, number of levels, and update the game board when the animal grids crushes.

--class variable: current level, current score, targetScore, a list of all the animal grids, a list of positions that are clicked, a list of crushingAnimals

--class method: gameStart(), checkSameType(), checkNeighbour(), checkSingleCrush(), swap(), update(), nextGame(), etc.


class AnimalModel:
--this class represents one specific animal grid, which is used to identify the type of animal grids and keep track of the position.  

--class variable: row, col, type, imagePattern(the image of the animal)

--class method: getRow(), getAnimalType(), etc.

subclass of Lion, Deer, Dog, Cat, Tiger, Rabbit, Giraffe
