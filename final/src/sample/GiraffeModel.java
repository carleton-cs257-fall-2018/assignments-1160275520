package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class GiraffeModel extends AnimalModel{

    public GiraffeModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image giraffe = new Image("animals/giraffe.png");
        ImagePattern giraffePattern = new ImagePattern(giraffe);
        return giraffePattern;
    }

    public String getType(){
        return "giraffe";
    }
}
