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
//import org.jetbrains.annotations.NotNull;
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
    }


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
