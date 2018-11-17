/**
 * Controller.java
 * Yuting Su, Starr Wang, 2018
 *
 * The Controller for this MVC sample application based on the game Animal Crush.
 */

package sample;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.Node;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;

import javafx.fxml.FXML;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.RowConstraints;
import org.jetbrains.annotations.NotNull;
import javafx.scene.image.Image ;
import javafx.scene.image.ImageView;


public class Controller {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private AnimalCrushView AnimalCrushView;
    @FXML private GridPane grid;

    private GameboardModel gameboardModel;

    public Controller() {
    }

    public void initialize() {
        this.gameboardModel = new GameboardModel(8, 8);
        this.update();

//        int numCols = 8 ;
//        int numRows = 8 ;
//
//        for (int i = 0 ; i < numCols ; i++) {
//            ColumnConstraints colConstraints = new ColumnConstraints();
//            colConstraints.setHgrow(Priority.SOMETIMES);
//            grid.getColumnConstraints().add(colConstraints);
//        }
//
//        for (int i = 0 ; i < numRows ; i++) {
//            RowConstraints rowConstraints = new RowConstraints();
//            rowConstraints.setVgrow(Priority.SOMETIMES);
//            grid.getRowConstraints().add(rowConstraints);
//        }
//
//        for (int i = 0 ; i < numCols ; i++) {
//            for (int j = 0; j < numRows; j++) {
//                addPane(i, j);
//            }
//        }

    }

//    private void addPane(int colIndex, int rowIndex) {
//        GridPane pane = new GridPane();
//        pane.setOnMouseClicked(e -> {
//            System.out.printf("Mouse enetered cell [%d, %d]%n", colIndex, rowIndex);
//        });
//        grid.add(pane, colIndex, rowIndex);
//    }

    public double getBoardWidth() {
        return AnimalCrushView.CELL_WIDTH * 8;
    }

    public double getBoardHeight() {
        return AnimalCrushView.CELL_WIDTH * 8;
    }

    private void update() {
        this.AnimalCrushView.update(this.gameboardModel);
        this.scoreLabel.setText(String.format("Score: %d", this.gameboardModel.getScore()));
        if (this.gameboardModel.isGameOver()) {
            this.messageLabel.setText("Congratulation!");
        }
        else {
            this.gameboardModel.update();
        }
    }
}
