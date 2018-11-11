package sample;

import java.util.Random;


public class GameboardModel {

    private int score;
    private GridModel[][] grids;
    private boolean gameOver;

    public GameboardModel(int rowCount, int columnCount) {
        assert rowCount > 0 && columnCount > 0;
        this.grids = new GridModel[rowCount][columnCount];
        this.gameStart();
    }

    public int getRowCount() {
        return this.grids.length;
    }

    public int getColumnCount() {
        assert this.grids.length > 0;
        return this.grids[0].length;
    }

    public GridModel[][] getGrids() {
        return this.grids;
    }

    public int getScore() {
        return this.score;
    }

    public boolean isGameOver() {
        return this.gameOver;
    }


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

    public void update(){
        this.swapGrid();
        this.updateGameBoard();
        this.updateScore();
    }

}
