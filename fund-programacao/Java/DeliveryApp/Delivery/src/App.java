import java.util.ArrayList;
import java.util.Scanner;

import javafx.animation.ScaleTransition;

public class App {

    Restaurante rest;
    Usuario user;

    ArrayList<Restaurante> rests = new ArrayList<>();
    ArrayList<Usuario> users = new ArrayList<>();
    ArrayList<String> pedido = new ArrayList<>();

    void addRest(Restaurante rest){
        this.rests.add(rest);
    }

    void remoRest(Restaurante rest){
        this.rests.remove(rest);
    }

    ArrayList<ArrayList> printRest(){
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

    void addUser(Usuario user){
        this.users.add(user);
    }

    void remoUser(Usuario user){
        this.users.remove(user);
    }
    
    void Pedido(){
        Scanner input = new Scanner(System.in);
        int haha = input.nextInt();
        if(users.indexOf(haha) != -1) {
            System.out.println();
        }else{
            System.out.println("Usuário nao encontrado!");
        }
    }

}
