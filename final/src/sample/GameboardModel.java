/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The Gameboard Model for this MVC sample application based on the game Animal Crush.
 */

package sample;
import java.util.Random;
import java.util.*;


public class GameboardModel {

    private int score;
    private AnimalModel[][] animals;
    private boolean gameOver;
    private List<Integer> firstClickedAnimal;


    /**
     * Class constructor
     * @param  rowCount the number of rows of the animals in the game board
     * @param  columnCount the number of columns of the animals in the game board
     */
    public GameboardModel(int rowCount, int columnCount) {
        assert rowCount > 0 && columnCount > 0;
        this.animals = new AnimalModel[rowCount][columnCount];
        this.gameStart();
        this.firstClickedAnimal = new ArrayList<>();
    }

    //a method that is called when the user click the animal grid
    public void userClickAnimal(int colIndex, int rowIndex){
        if (this.firstClickedAnimal.isEmpty()){
            this.firstClickedAnimal.add(rowIndex);
            this.firstClickedAnimal.add(colIndex);
        }
        else{
            if (checkNeighbour(colIndex, rowIndex, firstClickedAnimal.get(1), firstClickedAnimal.get(0))){
                System.out.printf("neighbours!");
            }
            if (checkSameType(colIndex, rowIndex, firstClickedAnimal.get(1), firstClickedAnimal.get(0))){
                System.out.printf("same animals!");
            }
        }
    }

    public boolean checkNeighbour(int col1, int row1, int col2, int row2){
        return ((col1==col2 && Math.abs(row1-row2)==1) || (row1==row2 && Math.abs(col1-col2)==1));
    }

    public boolean checkSameType(int col1, int row1, int col2, int row2){
        AnimalModel animal1 = animals[row1][col1];
        AnimalModel animal2 = animals[row2][col2];
        return (animal1.getType()==animal2.getType());
    }


    /**
     * A method to find the number of rows in the animals of the game board
     * @return  the number of rows of the animals in the game board
     */
    public int getRowCount() {
        return this.animals.length;
    }

    /**
     * A method to find the number of columns in the animals of the game board
     * @return  the number of columns of the animals in the game board
     */
    public int getColumnCount() {
        assert this.animals.length > 0;
        return this.animals[0].length;
    }

    /**
     * A method to get the animals, which is an array of an array of AnimalModel
     * @return  the animals that is created above
     */
    public AnimalModel getAnimal(int row, int col) {
        return this.animals[row][col];
    }

    /**
     * A method to get the current score that the users have achieved
     * @return  the number of current score
     */
    public int getScore() {
        return this.score;
    }

    /**
     * A method to check if the game is over
     * @return  a boolean where true means the game is over
     */
    public boolean isGameOver() {
        return this.gameOver;
    }

    /**
     * A method to find the number of rows in the animals of the game board
     * @return  the number of rows of the animals in the game board
     */

    public void gameStart() {
        this.score = 0;
        this.initializeGameboard();
    }

    /**
     * initialize the gameboard, randomly assign an animal type to each grid,
     * store the animals information to the class variable animals
     */
    private void initializeGameboard() {
        int rowCount = this.animals.length;
        int columnCount = this.animals[0].length;
        for (int col=0; col<columnCount; col++){
            for (int row=0; row<rowCount; row++){
                Random random = new Random();
                int num =  random.nextInt(5);
                if (num==0){
                    this.animals[row][col] = new DogModel(row, col);
                }
                else if(num==1){
                    this.animals[row][col] = new CatModel(row, col);
                }
                else if(num==2){
                    this.animals[row][col] = new DeerModel(row, col);
                }
                else if(num==3){
                    this.animals[row][col] = new LionModel(row, col);
                }
                else if(num==4){
                    this.animals[row][col] = new TigerModel(row, col);
                }
            }
        }
    }

    /**
     * when users click two animals, we need to check if each grid has matching animals nearby
     *
     * @param grid1 the first animal grid that the user clicks
     * @param grid2 the second animal grid that the user clicks
     * @return      the number of matching animals
     */
    public int checkCrush(AnimalModel grid1, AnimalModel grid2) {
        String animal1 = grid1.getType();
        String animal2 = grid2.getType();

        AnimalModel temp = new AnimalModel(grid2.getRow()+1, grid2.getCol());
        while(temp.getType().equals(animal1)){

        }
        return -1;
    }

    /**
     * swap two animal animals by switching their positions and animal types
     */
    public void swapGrid() {
    }

    /**
     * update the gameboard by replacing the matching animals with the ones above them
     * and filling the empty animals with new animals
     */
    public void updateGameBoard() {
    }


    /**
     * update the score according the number of matching animals that the user find
     */
    public void updateScore() {
    }

    /**
     * a method that groups the three methods which are required whenever there is matching animals
     */
    public void update(){
        this.swapGrid();
        this.updateGameBoard();
        this.updateScore();
    }
}