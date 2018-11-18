package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class DogModel extends AnimalModel{

    public DogModel(int row, int col){
        super(row, col);
    }

    public ImagePattern getImage(){
        Image dog = new Image("animals/dog.jpg");
        ImagePattern dogPattern = new ImagePattern(dog);
        return dogPattern;
    }

    public String getType(){
        return "dog";
    }
}
