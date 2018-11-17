package sample;

public class DeerModel extends AnimalModel {
    private String color;

    public DeerModel(int row, int col){
        super(row, col);
        this.color = "green";
    }

    public String getColor(){
        return this.color;
    }
}
