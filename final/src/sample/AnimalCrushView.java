/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The View for this MVC sample application based on the game Animal Crush.
 */

package sample;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class AnimalCrushView extends Group {
    public final static double CELL_WIDTH = 20.0;
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

    

    public void update(GameboardModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;

//        GameboardModel.List<List<GridModel>> grids = model.getGrids();
//        for (int row = 0; row < this.rowCount; row++) {
//            for (int column = 0; column < this.columnCount; column++) {
//                GridModel.animal animalType = grids[rowCount][columnCount];
//                if (animalType == GridModel.animal.DOG) {
//                    this.cellViews[row][column].setFill(Color.RED);
//                } else if (animalType == GridModel.animal.CAT) {
//                    this.cellViews[row][column].setFill(Color.BLACK);
//                } else if (animalType == GridModel.animal.DEER) {
//                    this.cellViews[row][column].setFill(Color.GREEN);
//                } else if (animalType == GridModel.animal.LION) {
//                    this.cellViews[row][column].setFill(Color.WHITE);
//                }
//            }
//        }
    }
}
