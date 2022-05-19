import java.util.ArrayList;
import java.util.Scanner;

public class Pedido {
    String user;
    Restaurante restaurante;

    ArrayList<Lanche> itens = new ArrayList<>(); 

    public Pedido(String user, Restaurante restaurante){
        this.user = user;
        this.restaurante = restaurante;
    }

    public void addItem() {
        System.out.println(restaurante.card);
    }
}
