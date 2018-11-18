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
    List<AnimalModel> crushingAnimals;

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
        this.crushingAnimals= new ArrayList<>();
    }

    //a method that is called when the user click the animal grid, return the index of two swapging animals
    public List<Integer> userClickAnimal(int colIndex, int rowIndex){
        if (this.firstClickedAnimal.isEmpty()){
            this.firstClickedAnimal.add(rowIndex);
            this.firstClickedAnimal.add(colIndex);
        }
        else{
            if (checkNeighbour(colIndex, rowIndex, firstClickedAnimal.get(1), firstClickedAnimal.get(0))
                    && !checkSameType(colIndex, rowIndex, firstClickedAnimal.get(1), firstClickedAnimal.get(0)))
            {
                this.checkCrush(firstClickedAnimal.get(0), firstClickedAnimal.get(1),rowIndex, colIndex);
                int number = checkCrush(rowIndex, colIndex, firstClickedAnimal.get(0), firstClickedAnimal.get(1));
                System.out.printf(Integer.toString(number));
                this.update();
                this.firstClickedAnimal.add(rowIndex);
                this.firstClickedAnimal.add(colIndex);
            }
        }
        return this.firstClickedAnimal;
    }

    private boolean checkNeighbour(int col1, int row1, int col2, int row2){
        return ((col1==col2 && Math.abs(row1-row2)==1) || (row1==row2 && Math.abs(col1-col2)==1));
    }

    private boolean checkSameType(int col1, int row1, int col2, int row2){
        AnimalModel animal1 = animals[row1][col1];
        AnimalModel animal2 = animals[row2][col2];
        return (animal1.getType()==animal2.getType());
    }

    private void checkUpwards(int originalRow, int originalCol, int swapRow, int swapCol){
        AnimalModel animal = animals[originalRow][originalCol];
        for (int row = swapRow - 1; row > 0; row--)
        {
            AnimalModel nearbyAnimal = animals[row][swapCol];
            if (nearbyAnimal.getType() == animal.getType()) {
                crushingAnimals.add(nearbyAnimal);
            } else {
                break;
            }
        }
    }

    private void checkDownwards(int originalRow, int originalCol, int swapRow, int swapCol){
        AnimalModel animal = animals[originalRow][originalCol];
        for (int row = swapRow+1; row< this.animals.length; row++)
        {
            AnimalModel nearbyAnimal = animals[row][swapCol];
            if (nearbyAnimal.getType() == animal.getType())
            {
                crushingAnimals.add(nearbyAnimal);
            }
            else{
                break;
            }
        }
    }

    private void checkLeftwards(int originalRow, int originalCol, int swapRow, int swapCol){
        AnimalModel animal = animals[originalRow][originalCol];
        for (int col = swapCol - 1; col > 0; col--)
        {
            AnimalModel nearbyAnimal = animals[swapRow][col];
            if (nearbyAnimal.getType() == animal.getType()) {
                crushingAnimals.add(nearbyAnimal);
            } else {
                break;
            }
        }
    }

    private void checkRightwards(int originalRow, int originalCol, int swapRow, int swapCol){
        AnimalModel animal = animals[originalRow][originalCol];
        for (int col = swapCol+1; col< this.animals[0].length; col++)
        {
            AnimalModel nearbyAnimal = animals[swapRow][col];
            if (nearbyAnimal.getType() == animal.getType())
            {
                crushingAnimals.add(nearbyAnimal);
            }
            else{
                break;
            }
        }
    }

    private int checkCrush(int originalRow, int originalCol, int swapRow, int swapCol){

        //if going up, check up, right, left
        if (swapCol==originalCol &&  originalRow-swapRow==1){
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going down, check down, right, left
        if (swapCol==originalCol &&  originalRow-swapRow==-1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going right, check down, up, right
        if (swapRow==originalRow &&  originalCol-swapCol==-1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going left, check down, up, left
        if (swapRow==originalRow &&  originalCol-swapCol==1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        return crushingAnimals.size();
    }

    public void update(){
        this.updateScore();
    }

    private void updateScore(){
        this.score = score + this.crushingAnimals.size();

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

    public List<AnimalModel> getCrushingAnimals(){
        return this.crushingAnimals;
    }
}