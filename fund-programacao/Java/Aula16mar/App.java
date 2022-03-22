import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner entrada = new Scanner(System.in);
        String valor="";
        do{
        System.out.println("Diga-me algo: ");
        valor = entrada.nextLine();
        }while(!valor.equalsIgnoreCase(valor = "algo"));
        entrada.close();
    }
}