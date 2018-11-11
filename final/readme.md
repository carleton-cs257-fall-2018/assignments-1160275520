The names of the partners working on this project.

A brief description (no more than one paragraph) of your project.

A brief argument of why MVC (or MVP, or a related pattern) is appropriate for your chosen project. This argument should make clear what your project's Model would consist of, and what its Views would be.

A list of the core classes that make up your Model.

[Optional] If you would like feedback on your program's intended user interface, you may include one or more mockups. (If you do this, please make your readme is a PDF file and include the mockups in the PDF. I'll be working quickly to give feedback on the projects, and I'd like to only have to open one documentation file.)



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

--class variable: score, grids

--class method: gameStart(), gameOver(), checkCrush(), swapGrid(), updateGameBoard(), updateScore()


class Grid:
--this class represents one specific animal grid, which is used to identify the type of animal grids and keep track of the position.  

--class variable: position, animalType 

--class method: getPosition(), getAnimalType(), 


updateGameBoard(replace the matching grids with the ones above them, fill the empty grids with new grids)
