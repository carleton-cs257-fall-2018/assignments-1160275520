package sample;

public class LionModel extends AnimalModel{

    private String color;

    public LionModel(int row, int col){
        super(row, col);
        this.color = "blue";
    }

    public String getColor(){
        return this.color;
    }

}
