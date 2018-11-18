package sample;

public class DogModel extends AnimalModel{

    private String type;

    public DogModel(int row, int col){
        super(row, col);
        this.type = "dog";
    }

    public String getType(){
        return this.type;
    }
}
