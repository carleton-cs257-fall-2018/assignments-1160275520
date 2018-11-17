package sample;

public class TigerModel extends AnimalModel{

    private String color;

    public TigerModel(int row, int col){
        super(row, col);
        this.color = "pink";
    }

    public String getColor(){
        return this.color;
    }
}
