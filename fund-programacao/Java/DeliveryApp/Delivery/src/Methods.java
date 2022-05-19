import java.util.ArrayList;
import java.util.Scanner;

public class Methods {

    Restaurante rest;
    Usuario user;

    ArrayList<Restaurante> rests = new ArrayList<>();
    ArrayList<Usuario> users = new ArrayList<>();
    ArrayList<String> pedido = new ArrayList<>();

    public void addRest(Restaurante rest){
        this.rests.add(rest);
        System.out.println("Restaurante adicionado!");
    }

    public void remoRest(Scanner input){
        int ind = this.ChooseRest(input);
        this.rests.remove(ind);
        System.out.println("Restaurante removido!");
    }

    public int ChooseRest(Scanner input){
        System.out.println("Selecione o restaurante: ");
        System.out.println(this.printRest());
        int ind = Integer.parseInt(input.nextLine());
        return ind;
    }

    public ArrayList<ArrayList> printRest(){
        ArrayList<ArrayList> restaurantes = new ArrayList<>();
        for(Restaurante rest : rests){
            ArrayList<Object> restArray = new ArrayList<>();
            restArray.add(rest.name);
            restArray.add(rest.cnpj);
            restArray.add(rest.loc);
            restaurantes.add(restArray);
        }
        return restaurantes;
    }
    public int restSelect(Scanner input){
        System.out.println("Digite o index do restaurante: ");
        System.out.println(this.printRest());
        int ind = Integer.parseInt(input.nextLine());
        return ind;
    }

    public ArrayList<ArrayList> printUsers(){
        ArrayList<ArrayList> usuarios = new ArrayList<>();
        for(Usuario user : users){
            ArrayList<Object> usersArray = new ArrayList<>();
            usersArray.add(user.name);
            usersArray.add(user.end);
            usersArray.add(user.cpf);
            usuarios.add(usersArray);
        }
        return usuarios;
    }

    void addUser(Usuario user){
        this.users.add(user);
        System.out.println("Usuario cadastrado!");
    }

    void remoUser(Usuario user){
        this.users.remove(user);
        System.out.println("Usuario removido!");
    }
    
    public void listOrder(String user) {
        for (Usuario usuario : users) {
            if (usuario.name.equals(user)) {
                usuario.printPedidos();
            }
        }
    }
    public void makeOrder(Scanner input, String user) {
        for (Usuario usuario : users) {
            if (usuario.name.equals(user)) {
                int ind = this.ChooseRest(input);
                if (ind != -1) {
                    System.out.println("Digite o nome do pedido: ");
                    String nomePedido = input.nextLine();
                    usuario.adicionarPedido(input, nomePedido, rests.get(ind));
                }
            }
        }
    }
    public void cadastrarUsuario(Usuario user) {
        System.out.println("Cadastrando usuário...");
        boolean validation = false;
        for (Usuario usuario : users) {
            if (usuario.name.equals(usuario.name))
                validation = true;
        }
        if (validation == false)
            this.users.add(user);
        else
            System.out.println("Usuario ja cadastrado!");
    }

    void imprimirCardapioRestaurante(Scanner input) {
        System.out.println("Digite o indice do restaurante para saber o cardapio: ");
        System.out.println(this.printRest());
        int ind = Integer.parseInt(input.nextLine());
        this.rests.get(ind).printCard();
    }

    void imprimirCardapioRestaurante(Scanner input, int restauranteIndex) {
        this.rests.get(restauranteIndex).printCard();
    }

    void adicionarItemsRestaurante(Scanner input, Lanche lanche) {
        System.out.println("Digite o indice do restaurante para adicionar o lanche: ");
        System.out.println(this.printRest());
        int ind = Integer.parseInt(input.nextLine());
        this.rests.get(ind).addLanche(lanche);
    }

    void adicionarItemsRestaurante(Lanche lanche, int restauranteIndex) {
        this.rests.get(restauranteIndex).addLanche(lanche);
    }

    void removerItemsRestaurante(Scanner input) {
        System.out.println("Digite o indice do rest que deseja remover o lanche: ");
        System.out.println(this.printRest());
        int resInd = Integer.parseInt(input.nextLine());
        System.out.println("Digite o indice do lanche no cardapio para remover: ");
        this.imprimirCardapioRestaurante(input, resInd);
        int ind = Integer.parseInt(input.nextLine());
        this.rests.get(resInd).remoInd(ind);
    }

    void removerItemsRestaurante(Scanner input, int restauranteIndex) {
        System.out.println("Digite o indice do lanche no cardapio para remover: ");
        this.imprimirCardapioRestaurante(input, restauranteIndex);
        int ind = Integer.parseInt(input.nextLine());
        this.rests.get(restauranteIndex).remoInd(ind);
    }
    public boolean userAuth(String user) {
        for (Usuario usuario : users) {
            if (usuario.name.equals(user))
                return true;
        }
        return false;
    }
}
