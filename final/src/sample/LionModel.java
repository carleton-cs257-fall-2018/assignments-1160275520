package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class LionModel extends AnimalModel{

    public LionModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image lion = new Image("animals/lion.jpg");
        ImagePattern lionPattern = new ImagePattern(lion);
        return lionPattern;
    }

    public String getType(){
        return "lion";
    }
}
