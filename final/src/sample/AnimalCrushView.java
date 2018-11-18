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
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Random;

import javafx.fxml.FXML;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.RowConstraints;


public class AnimalCrushView extends Group {
    public final static double CELL_WIDTH = 90.0;
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
                    int colIndex = column;
                    int rowIndex = row;
                    rectangle.setOnMouseClicked(e -> {
                        int[] first = [rowIndex, colIndex];
                        int[] second = []
                        System.out.printf("Mouse enetered cell [%d, %d]%n", colIndex, rowIndex);

                    });
                    this.getChildren().add(rectangle);
                }
            }
        }
    }


    public void update(GameboardModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                AnimalModel animal = model.getAnimal(row,column);
                if (animal.getColor() == "red") {
                    this.cellViews[row][column].setFill(Color.RED);
                }
                else if (animal.getColor() == "yellow") {
                    this.cellViews[row][column].setFill(Color.YELLOW);
                }
                else if (animal.getColor() == "blue") {
                    this.cellViews[row][column].setFill(Color.BLUE);
                }
                else if (animal.getColor() == "green") {
                    this.cellViews[row][column].setFill(Color.GREEN);
                }
                else if (animal.getColor() == "pink") {
                    this.cellViews[row][column].setFill(Color.PINK);
                }
            }
        }

    }


}
