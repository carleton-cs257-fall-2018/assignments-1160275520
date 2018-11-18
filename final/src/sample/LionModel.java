package sample;

public class LionModel extends AnimalModel{

    private String color;
    private String type;

    public LionModel(int row, int col){
        super(row, col);
        this.color = "blue";
        this.type = "lion";
    }

    public String getColor(){
        return this.color;
    }

    public String getType() {
        return this.type;
    }
}
