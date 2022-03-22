package Aula03;
import java.util.Scanner;

public class string {
    public static void main(String[] args) throws Exception {
        String texto;
        try (Scanner entrada = new Scanner(System.in)){
            texto = entrada.nextLine();
        }    
        System.out.println(texto == "Like a Bosch");
        System.out.println(texto.equals("Like a Bosch"));
    }    
}