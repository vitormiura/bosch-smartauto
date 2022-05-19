import java.util.ArrayList;
//import java.util.Scanner;

public class Restaurante {
    String name;
    String cnpj;
    String loc;

    Lanche lanche;
    ArrayList<Lanche> card = new ArrayList<>();

    public Restaurante(String name, String cnpj, String loc){
        this.name = name;
        this.cnpj = cnpj;
        this.loc = loc;
    }

    void addLanche(Lanche lanche){
        this.card.add(lanche);
        lanche.restaurante = this;
    }

    void remoLanche(Lanche lanche){
        this.card.remove(lanche);
    }

    void remoInd(int index){
        this.card.remove(lanche);
    }

    public ArrayList<ArrayList> printCard(){
        ArrayList<ArrayList> lanches = new ArrayList<>();
        for(Lanche lanche : card){
            ArrayList<Object> lancheArray = new ArrayList<>();
            lancheArray.add(lanche.name);
            lancheArray.add(lanche.price);
            lanches.add(lancheArray);
        }
        return lanches;
    }

    
}
