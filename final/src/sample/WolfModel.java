package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class WolfModel extends AnimalModel{

    public WolfModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image wolf = new Image("animals/wolf.jpg");
        ImagePattern wolfPattern = new ImagePattern(wolf);
        return wolfPattern;
    }

    public String getType(){
        return "wolf";
    }
}
