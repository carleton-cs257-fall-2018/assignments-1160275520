package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class RabbitModel extends AnimalModel{

    public RabbitModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image rabbit = new Image("animals/rabbit.jpg");
        ImagePattern rabbitPattern = new ImagePattern(rabbit);
        return rabbitPattern;
    }

    public String getType(){
        return "rabbit";
    }
}