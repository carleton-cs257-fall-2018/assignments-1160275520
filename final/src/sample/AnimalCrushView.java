/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The View for this MVC sample application based on the game Animal Crush.
 */

package sample;

import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.ImagePattern;
import javafx.animation.Timeline;
import javafx.animation.KeyFrame;
import javafx.util.Duration;
import java.util.*;


public class AnimalCrushView extends Group {
    public final static double CELL_WIDTH = 80.0;
    @FXML private int rowCount;
    @FXML private int columnCount;
    private Rectangle[][] cellViews;

    public AnimalCrushView() {
    }

    public int getRowCount() {
        return this.rowCount;
    }

    public void setRowCount(int rowCount) {
        this.rowCount = rowCount;
        this.initializeGrid();
    }

    public int getColumnCount() {
        return this.columnCount;
    }

    public void setColumnCount(int columnCount) {
        this.columnCount = columnCount;
        this.initializeGrid();
    }

    private void initializeGrid() {
        if (this.rowCount > 0 && this.columnCount > 0) {
            this.cellViews = new Rectangle[this.rowCount][this.columnCount];
            for (int row = 0; row < this.rowCount; row++) {
                for (int column = 0; column < this.columnCount; column++) {
                    Rectangle rectangle = new Rectangle();
                    rectangle.setX((double)column * CELL_WIDTH);
                    rectangle.setY((double)row * CELL_WIDTH);
                    rectangle.setWidth(CELL_WIDTH);
                    rectangle.setHeight(CELL_WIDTH);
                    this.cellViews[row][column] = rectangle;
                    this.getChildren().add(rectangle);
                }
            }
        }
    }


    //This method update the game board view by giving each grid an animal picture and a function when user clicks
    public boolean update(GameboardModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {

                int colIndex = column;
                int rowIndex = row;
                Rectangle rectangle = this.cellViews[row][column];

                //When user clicks the grid, it triggers the userClick function in the game board model
                rectangle.setOnMouseClicked(e -> {
                    // it user clicks two animals
                    if (model.userClickAnimal(rowIndex, colIndex)){
                        //generate swapping effects in the view
                        this.swapAnimals(model.getClickedAnimalsPosition(),model);
                        //generate crushing effects in the view
                        this.crushingAnimals(model);

                        //update the model by swaping two animals, replacing crushing animals with new animal and updating the score

                        model.update();
                        model.clearUp();
                    }
                });

                //give each grid an animal picture
                AnimalModel animal = model.getAnimal(row,column);
                this.cellViews[row][column].setFill(animal.getImage());
            }
        }
    }

    private void swapAnimals(List<Integer> swapAnimalIndex, GameboardModel model){
        AnimalModel animal1 = model.getAnimal(swapAnimalIndex.get(0),swapAnimalIndex.get(1));
        AnimalModel animal2 = model.getAnimal(swapAnimalIndex.get(2),swapAnimalIndex.get(3));
        this.cellViews[animal1.getRow()][animal1.getCol()].setFill(animal2.getImage());
        this.cellViews[animal2.getRow()][animal2.getCol()].setFill(animal1.getImage());
    }

    private void crushingAnimals(GameboardModel model){
        List<AnimalModel> crushingAnimals = model.getCrushingAnimals();
        for (int index = 0; index<crushingAnimals.size(); index++){
            AnimalModel animal = crushingAnimals.get(index);
            Image bomb = new Image("animals/bomb.gif");
            ImagePattern bombPattern = new ImagePattern(bomb);
            //use the timeline to generate the crushing effects after the swapping effects
            Timeline timeline = new Timeline(new KeyFrame(Duration.millis(500), ae -> this.cellViews[animal.getRow()][animal.getCol()].setFill(bombPattern)));
            timeline.play();
        }
    }
}
