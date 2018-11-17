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

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader loader = new FXMLLoader(getClass().getResource("animalCrush.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("animal crush");

//        GridPane root = FXMLLoader.load(getClass().getResource("animalCrush.fxml"));
//        primaryStage.setScene(new Scene(root, 800, 800));
//        primaryStage.show();

        Controller controller = loader.getController();
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
