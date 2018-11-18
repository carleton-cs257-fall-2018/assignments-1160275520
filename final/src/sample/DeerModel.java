package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class DeerModel extends AnimalModel {

    public DeerModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image deer = new Image("animals/deer.jpg");
        ImagePattern deerPattern = new ImagePattern(deer);
        return deerPattern;
    }

    public String getType(){
        return "deer";
    }
}
