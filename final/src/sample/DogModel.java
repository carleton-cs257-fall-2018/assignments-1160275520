package sample;

public class DogModel extends AnimalModel{

    private String color;

    public DogModel(int row, int col){
        super(row, col);
        this.color = "yellow";
    }

    public String getColor(){
        return this.color;
    }
}
