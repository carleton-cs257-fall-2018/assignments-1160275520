/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The Grid Model for this MVC sample application based on the game Animal Crush.
 */

package sample;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class AnimalModel {
    List<Integer> position = new ArrayList<Integer>();
    String color;
    String type;

    /**
     * Class constructor
     * @param  row the row of the grid
     * @param  col the column of the grid
     */
    public AnimalModel(int row, int col) {
        this.position.add(row);
        this.position.add(col);
//        this.animalType = initializeAnimalType();
    }

    public String getColor(){
        return color;
    }

    public String getType() {
        return this.type;
    }

    public int getRow(){
        return this.position.get(0);
    }

    public int getCol(){
        return this.position.get(1);
    }

//    /**
//     * This method gives the grid a random animal type
//     */
//    public animal initializeAnimalType(){
//        Random random = new Random();
//        return animal.values()[new Random().nextInt(animal.values().length)];
//    }
//
//    /**
//     * This method get the position of the grid
//     */
//    public List<Integer> getPosition(){
//        return position;
//    }
//
//    /**
//     * This method get the animal type of the grid
//     */
//    public animal getAnimalType(){
//        return animalType;
//    }

}