package Bosch;

public class Main {

    public static void main(String[] args) {
        Usuario u = new Usuario();
        System.out.println(u.getIdade());
        u.setIdade(20);
        System.out.println(u.getIdade());
    }
}
