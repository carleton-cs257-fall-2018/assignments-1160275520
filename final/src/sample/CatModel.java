package sample;

public class CatModel extends AnimalModel{

    private String color;

    public CatModel(int row, int col){
        super(row, col);
        this.color = "red";
    }

    public String getColor(){
        return this.color;
    }
}
