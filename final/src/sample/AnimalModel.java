/**
 * AnimalCrushView.java
 * Yuting Su, Starr Wang, 2018
 *
 * The Grid Model for this MVC sample application based on the game Animal Crush.
 */

package sample;

import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class AnimalModel {
    private int row;
    private int col;
    private String type;
    private ImagePattern imagePattern;


    /**
     * Class constructor
     * @param  row the row of the grid
     * @param  col the column of the grid
     */
    public AnimalModel(int row, int col) {
        this.row=row;
        this.col=col;
    }

    public int getRow(){
        return this.row;
    }

    public int getCol(){
        return this.col;
    }

    public ImagePattern getImage(){
        return this.imagePattern;
    }

    public String getType(){
        return this.type;
    }
}