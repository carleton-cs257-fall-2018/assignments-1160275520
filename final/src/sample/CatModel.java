package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class CatModel extends AnimalModel{

    public CatModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image cat = new Image("animals/cat.jpg");
        ImagePattern catPattern = new ImagePattern(cat);
        return catPattern;
    }

    public String getType(){
        return "cat";
    }
}
