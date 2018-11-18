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
                    int colIndex = column;
                    int rowIndex = row;

                    rectangle.setOnMouseClicked(e -> {
                        Image bomb = new Image("animals/bomb.gif");
                        ImagePattern bombPattern = new ImagePattern(bomb);
                        this.cellViews[rowIndex][colIndex].setFill(bombPattern);
                        System.out.printf("Mouse enetered cell [%d, %d]%n", colIndex, rowIndex);

                    });
                    this.getChildren().add(rectangle);
                }
            }
        }
    }


    public void update(GameboardModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;

        Image cat = new Image("animals/cat.jpg");
        ImagePattern catPattern = new ImagePattern(cat);
        Image dog = new Image("animals/dog.jpg");
        ImagePattern dogPattern = new ImagePattern(dog);
        Image deer = new Image("animals/deer.jpg");
        ImagePattern deerPattern = new ImagePattern(deer);
        Image lion = new Image("animals/lion.jpg");
        ImagePattern lionPattern = new ImagePattern(lion);
        Image tiger = new Image("animals/tiger.jpg");
        ImagePattern tigerPattern = new ImagePattern(tiger);

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                AnimalModel animal = model.getAnimal(row,column);
                if (animal.getType() == "cat") {
                    this.cellViews[row][column].setFill(catPattern);
                }
                else if (animal.getType() == "dog") {
                    this.cellViews[row][column].setFill(dogPattern);
                }
                else if (animal.getType() == "lion") {
                    this.cellViews[row][column].setFill(lionPattern);
                }
                else if (animal.getType() == "deer") {
                    this.cellViews[row][column].setFill(deerPattern);
                }
                else if (animal.getType() == "tiger") {
                    this.cellViews[row][column].setFill(tigerPattern);
                }
            }
        }

    }


}
