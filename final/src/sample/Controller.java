package sample;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Controller {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private AnimalCrushView AnimalCrushView;
    private GameboardModel gameboardModel;

    public Controller() {
    }

    public void initialize() {
        this.gameboardModel = new GameboardModel(this.AnimalCrushView.getRowCount(), this.AnimalCrushView.getColumnCount());
        this.update();
    }

    public double getBoardWidth() {
        return AnimalCrushView.CELL_WIDTH * this.AnimalCrushView.getColumnCount();
    }

    public double getBoardHeight() {
        return AnimalCrushView.CELL_WIDTH * this.AnimalCrushView.getRowCount();
    }

    private void update() {
        this.AnimalCrushView.update(this.gameboardModel);
        this.scoreLabel.setText(String.format("Score: %d", this.gameboardModel.getScore()));
        if (this.gameboardModel.isGameOver()) {
            this.messageLabel.setText("Congratulation!You win the game");
        }
        else {
            this.gameboardModel.update();
        }
    }

    /**
     * this method handle the event when the user click two grids.
     */
    public void handle(KeyEvent keyEvent) {
        boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();
    }
}
