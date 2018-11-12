/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The Gameboard Model for this MVC sample application based on the game Animal Crush.
 */

package sample;
import java.util.Random;


public class GameboardModel {

    private int score;
    private GridModel[][] grids;
    private boolean gameOver;

    /**
     * Class constructor
     * @param  rowCount the number of rows of the grids in the game board
     * @param  columnCount the number of columns of the grids in the game board
     */
    public GameboardModel(int rowCount, int columnCount) {
        assert rowCount > 0 && columnCount > 0;
        this.grids = new GridModel[rowCount][columnCount];
        this.gameStart();
    }

    /**
     * A method to find the number of rows in the grids of the game board
     * @return  the number of rows of the grids in the game board
     */
    public int getRowCount() {
        return this.grids.length;
    }

    /**
     * A method to find the number of columns in the grids of the game board
     * @return  the number of columns of the grids in the game board
     */
    public int getColumnCount() {
        assert this.grids.length > 0;
        return this.grids[0].length;
    }

    /**
     * A method to get the grids, which is an array of an array of GridModel
     * @return  the grids that is created above
     */
    public GridModel[][] getGrids() {
        return this.grids;
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
     * A method to find the number of rows in the grids of the game board
     * @return  the number of rows of the grids in the game board
     */

    public void gameStart() {
        this.score = 0;
        this.initializeGameboard();
    }

    /**
     * initialize the gameboard, randomly assign an animal type to each grid,
     * store the grids information to the class variable grids
     */
    private void initializeGameboard() {
        int rowCount = this.grids.length;
        int columnCount = this.grids[0].length;
    }

    /**
     * when users click two grids, we need to check if each grid has matching grids nearby
     *
     * @param grid1 the first animal grid that the user clicks
     * @param grid2 the second animal grid that the user clicks
     * @return      the number of matching grids
     */
    public int checkCrush(GridModel grid1, GridModel grid2) {
        return -1;
    }

    /**
     * swap two animal grids by switching their positions and animal types
     */
    public void swapGrid() {
    }

    /**
     * update the gameboard by replacing the matching grids with the ones above them
     * and filling the empty grids with new grids
     */
    public void updateGameBoard() {
    }


    /**
     * update the score according the number of matching grids that the user find
     */
    public void updateScore() {
    }

    /**
     * a method that groups the three methods which are required whenever there is matching grids
     */
    public void update(){
        this.swapGrid();
        this.updateGameBoard();
        this.updateScore();
    }
}