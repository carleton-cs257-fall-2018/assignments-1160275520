package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class TigerModel extends AnimalModel{

    public TigerModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image tiger = new Image("animals/tiger.jpg");
        ImagePattern tigerPattern = new ImagePattern(tiger);
        return tigerPattern;
    }

    public String getType(){
        return "tiger";
    }
}
