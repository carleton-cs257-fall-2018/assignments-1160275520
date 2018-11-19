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
import javafx.scene.input.MouseEvent;
import javafx.scene.input.MouseButton;
import javafx.animation.Timeline;
import javafx.animation.KeyFrame;
import javafx.util.Duration;



public class Controller implements EventHandler<MouseEvent> {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private Label targetLabel;
    @FXML private AnimalCrushView AnimalCrushView;
    private int clickCount;
    private GameboardModel gameboardModel;


    public Controller() {
        clickCount = 0;
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
        this.targetLabel.setText(String.format("Target Score: %d", this.gameboardModel.getTargetScore()));
        this.messageLabel.setText(String.format("Level: %d", this.gameboardModel.getLevel()));
    }

    @Override
    public void handle(MouseEvent mouseEvent) {
        if(mouseEvent.getButton().equals(MouseButton.PRIMARY)){
            //if the user click two grids, update the animal crush view.
            clickCount +=1;
            if(clickCount == 2){
                Timeline timeline = new Timeline(new KeyFrame(Duration.millis(1000), ae -> this.update()));
                timeline.play();
                clickCount = 0;
                //if the game is over
                if (this.gameboardModel.isGameOver()) {
                    this.messageLabel.setText("Congratulations!");
                    //start the next game
                    this.gameboardModel.nextGame();
                    //update the animal crush view again
                    Timeline timeline2 = new Timeline(new KeyFrame(Duration.millis(10000), ae -> this.update()));
                    timeline2.play();
                }
            }
        }
    }
}
