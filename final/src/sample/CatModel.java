package sample;

public class CatModel extends AnimalModel{

    private String type;

    public CatModel(int row, int col){
        super(row, col);
        this.type = "cat";
    }

    public String getType(){
        return "cat";
    }
}
