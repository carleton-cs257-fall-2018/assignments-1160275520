package sample;

public class LionModel extends AnimalModel{

    private String type;

    public LionModel(int row, int col){
        super(row, col);
        this.type = "lion";
    }

    public String getType() {
        return this.type;
    }
}
