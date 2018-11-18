package sample;

public class DeerModel extends AnimalModel {
    private String type;

    public DeerModel(int row, int col){
        super(row, col);
        this.type = "deer";
    }

    public String getType(){
        return this.type;
    }
}
