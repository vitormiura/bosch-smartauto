import java.util.ArrayList;
import java.util.Scanner;

public class Usuario {
    String name;
    String end;
    String cpf;

    //public Restaurante restaurante;

    public Usuario(String name, String end, String cpf){
        this.name = name;
        this.end = end;
        this.cpf = cpf;
    }

    ArrayList<Pedido> pedidos = new ArrayList<>();

    public ArrayList<ArrayList> printPedidos(){
        ArrayList<ArrayList> pedis = new ArrayList<>();
        for(Pedido pedido : pedidos){
            ArrayList<Object> pediArr = new ArrayList<>();
            pediArr.add(pedido.user);
            pedis.add(pediArr);
        }
        return pedis;
    }

    public void adicionarPedido(Scanner input, String nome, Restaurante restaurante) {
        pedidos.add(new Pedido(nome, restaurante));
        while (true) {
            System.out.println("Selecione o lanche: ");
            restaurante.printCard();
            System.out.println("\nDeseja outro lanche? (s/n): ");
            String op = input.nextLine();
            if (op == "n")
                break;
        }
    }
}
