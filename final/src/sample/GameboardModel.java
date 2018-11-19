/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * This Model class represents the whole gameboard, which is used to keep track of the score, all the animal grids, etc.
\ */

package sample;
import java.util.Random;
import java.util.*;


public class GameboardModel {

    private int score;
    private int targetScore;
    private AnimalModel[][] animals; //all the animal grids
    private List<Integer> clickedAnimalsPosition; //the position of the two animals that the user clicks
    private List<AnimalModel> crushingAnimals; //all the matching animals that need to be replaced
    private int currentLevel;

    
    public GameboardModel(int rowCount, int columnCount) {
        assert rowCount > 0 && columnCount > 0;
        this.animals = new AnimalModel[rowCount][columnCount];
        this.clickedAnimalsPosition = new ArrayList<>();
        this.crushingAnimals= new ArrayList<>();
        this.currentLevel = 1;
        this.gameStart();
    }

    public int getRowCount() {
        return this.animals.length;
    }

    public int getColumnCount() {
        assert this.animals.length > 0;
        return this.animals[0].length;
    }

    public AnimalModel getAnimal(int row, int col) {
        return this.animals[row][col];
    }

    public List<AnimalModel> getCrushingAnimals(){
        return this.crushingAnimals;
    }

    public List<Integer> getClickedAnimalsPosition(){
        return  this.clickedAnimalsPosition;
    }

    public int getScore() {
        return this.score;
    }
    public int getTargetScore() {
        return this.targetScore;
    }
    public int getLevel() {
        return this.currentLevel;
    }

    /**
     * A method to check if the game is over
     * @return  a boolean where true means the game is over
     */
    public boolean isGameOver() {
        return score >= targetScore;

    }

    public void gameStart() {
        this.score = 0;
        this.targetScore = currentLevel*5;
        this.initializeGameboard();
    }

    public void nextGame(){
        this.currentLevel++;
        this.gameStart();
    }

    /**
     * this method initialize the gameboard by randomly assigning an animal type to each grid,
     * and storing the animals information to the class variable animals
     */
    private void initializeGameboard() {
        int rowCount = this.animals.length;
        int columnCount = this.animals[0].length;
        for (int row=0; row<rowCount; row++){
            for (int col=0; col<columnCount; col++){
                randomSetAnimals(row, col);
            }
        }
    }

    /**
     * This method handle the event when the user click an animal grid
     * @param  colIndex the column of the animals in the game board
     * @param  rowIndex the row of the animal in the game board
     * return True if the gameboard needs to change
     * return False if the gameboard remains the same
     */
    public Boolean userClickAnimal(int rowIndex, int colIndex){
        //add the animal to the list
        this.clickedAnimalsPosition.add(rowIndex);
        this.clickedAnimalsPosition.add(colIndex);

        //if this is the first animal that the user click, return false
        if (this.clickedAnimalsPosition.size()==2){
            return false;
        }
        //Otherwise
        else{
            //checks if the two animal are of the same type and are neighbours.
            if (checkNeighbour() && !checkSameType())
            {
                //if yes, check the matching animals that need to be replaced and add them to the list
                this.checkAllCrush(clickedAnimalsPosition.get(0), clickedAnimalsPosition.get(1),rowIndex, colIndex);
                return true;
            }
            //otherwise, clear the clicked animal list.
            else {
                this.clickedAnimalsPosition.clear();
            }
        }
        return false;
    }

    private boolean checkNeighbour(){
        int row1 = this.clickedAnimalsPosition.get(0);
        int col1 = this.clickedAnimalsPosition.get(1);
        int row2 = this.clickedAnimalsPosition.get(2);
        int col2 = this.clickedAnimalsPosition.get(3);

        return ((col1==col2 && Math.abs(row1-row2)==1) || (row1==row2 && Math.abs(col1-col2)==1));
    }

    private boolean checkSameType(){
        AnimalModel animal1 = animals[this.clickedAnimalsPosition.get(0)][this.clickedAnimalsPosition.get(1)];
        AnimalModel animal2 = animals[this.clickedAnimalsPosition.get(2)][this.clickedAnimalsPosition.get(3)];
        return (animal1.getType()==animal2.getType());
    }

    /**
     * This methods check all the crushing after the user clicks two animal
     * @param  row1 the row of the first animal that the user click
     * @param  col1 the column of the first animal that the user click
     * @param  row2 the row of the second animal that the user click
     * @param  col2 the column of the second animal after swap
     */
    private void checkAllCrush(int row1, int col1, int row2, int col2){
        checkSingleCrush(row1, col1, row2, col2);
        checkSingleCrush(row2, col2, row1, col1);
    }

    /**
     * This methods check if the animal will cause crushing after the user swaps it to a new position
     * @param  originalRow the original row of the animals before swap
     * @param  originalCol the original column of the animal before swap
     * @param  swapRow the new row of the animals after swap
     * @param  swapCol the new column of the animal after swap
     */
    private void checkSingleCrush(int originalRow, int originalCol, int swapRow, int swapCol){

        int originalSize = crushingAnimals.size();
        //if going up, check up, right, left
        if (swapCol==originalCol &&  originalRow-swapRow==1){
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going down, check down, right, left
        else if (swapCol==originalCol &&  originalRow-swapRow==-1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going right, check down, up, right
        else if (swapRow==originalRow &&  originalCol-swapCol==-1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkRightwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if going left, check down, up, left
        else if (swapRow==originalRow &&  originalCol-swapCol==1){
            this.checkDownwards(originalRow, originalCol, swapRow, swapCol);
            this.checkUpwards(originalRow, originalCol, swapRow, swapCol);
            this.checkLeftwards(originalRow, originalCol, swapRow, swapCol);
        }

        //if the original animal causes crushing, add the animal into crushing animal list
        if(crushingAnimals.size() != (originalSize)) {
            crushingAnimals.add(getAnimal(originalRow, originalCol));
        }
    }

    /**
     * The below four methods check if the animal matches in four different direction
     * @param  originalRow the original row of the animals before swap
     * @param  originalCol the original column of the animal before swap
     * @param  swapRow the new row of the animals after swap
     * @param  swapCol the new column of the animal after swap
     */

    private void checkUpwards(int originalRow, int originalCol, int swapRow, int swapCol){
        //get the original animal
        AnimalModel animal = animals[originalRow][originalCol];
        for (int row = swapRow-1; row >= 0; row--)
        {
            //get the new animal
            AnimalModel nearbyAnimal = animals[row][swapCol];
            //if they are matching, add it to the crushing animal list
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
        for (int col = swapCol - 1; col >= 0; col--)
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
    

    //this method update the whole gameboad by swaping two animals that the user clicks
    //updating the score, replacing the crushing animal with new animals
    //and clear up the crushingAnimalList and clickedAnimalList
    public void update(){
        this.updateScore();
        this.swap();
        this.replaceWithNewAnimal();
        this.clearUp();
    }

    //this method swap two animals
    public void swap(){
        if (this.clickedAnimalsPosition.size()==4 && this.crushingAnimals.size()!=0){
            int row1 = this.clickedAnimalsPosition.get(0);
            int col1 = this.clickedAnimalsPosition.get(1);
            int row2 = this.clickedAnimalsPosition.get(2);
            int col2 = this.clickedAnimalsPosition.get(3);

            AnimalModel animal1 = animals[row1][col1];
            AnimalModel animal2 = animals[row2][col2];

            animal1.setPosition(row2,col2);
            animal2.setPosition(row1,col1);

            animals[row1][col1] = animal2;
            animals[row2][col2] = animal1;
        }
    }

    private void updateScore(){
        this.score = score + this.crushingAnimals.size();
    }

    //this method replace the crushing animals with new random animals
    private void replaceWithNewAnimal(){
        for(int i = 0; i < crushingAnimals.size(); i++){
            int tempRow = crushingAnimals.get(i).getRow();
            int tempCol = crushingAnimals.get(i).getCol();
            randomSetAnimals(tempRow, tempCol);
        }
    }

    private void randomSetAnimals(int row, int col){
        Random random = new Random();
        int num =  random.nextInt(8);
        if (num==6){
            this.animals[row][col] = new DogModel(row, col);
        }
        else if(num==7){
            this.animals[row][col] = new GiraffeModel(row, col);
        }
        else if(num==5){
            this.animals[row][col] = new WolfModel(row, col);
        }
        else if(num==4){
            this.animals[row][col] = new CatModel(row, col);
        }
        else if(num==3){
            this.animals[row][col] = new DeerModel(row, col);
        }
        else if(num==2){
            this.animals[row][col] = new LionModel(row, col);
        }
        else if(num==1){
            this.animals[row][col] = new TigerModel(row, col);
        }
        else if(num==0){
            this.animals[row][col] = new RabbitModel(row, col);
        }

    }

    //this method reset the clickedAnimalsList and crushingAnimalList
    public void clearUp(){
        clickedAnimalsPosition.clear();
        crushingAnimals.clear();
    }
}