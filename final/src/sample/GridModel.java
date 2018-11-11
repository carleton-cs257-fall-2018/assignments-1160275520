package sample;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class GridModel {
    List<Integer> position = new ArrayList<Integer>();
    private animal animalType;

    public enum animal {
        DOG, CAT, DEER, LION
    };

    public GridModel(int xcoordinate, int ycoordinate) {
        this.position.add(xcoordinate);
        this.position.add(ycoordinate);
        this.animalType = initializeAnimalType();
    }

    public animal initializeAnimalType(){
        Random random = new Random();
        return animal.values()[new Random().nextInt(animal.values().length)];
    }

    public List<Integer> getPosition(){
        return position;
    }

    public animal getAnimalType(){
        return animalType;
    }

}
