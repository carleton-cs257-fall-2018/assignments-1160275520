package sample;

public class TigerModel extends AnimalModel{

    private String type;

    public TigerModel(int row, int col){
        super(row, col);
        this.type = "tiger";
    }

    public String getType(){
        return this.type;
    }
}
