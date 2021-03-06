/**
 * Controller.java
 * Yuting Su, Starr Wang, 2018
 *
 * The JavaFX Application class and main program for this MVC sample application
 * based on the game Animal Crush.
 */


package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import javafx.scene.input.MouseEvent;
import javafx.scene.input.MouseButton;


public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader loader = new FXMLLoader(getClass().getResource("animalCrush.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("animal crush");

        Controller controller = loader.getController();
        root.setOnMouseClicked(controller);
        double sceneWidth = controller.getBoardWidth() + 20.0;
        double sceneHeight = controller.getBoardHeight() + 100.0;
        primaryStage.setScene(new Scene(root, sceneWidth, sceneHeight));
        primaryStage.show();
        root.requestFocus();

    }


    public static void main(String[] args) {
        launch(args);
    }
}
