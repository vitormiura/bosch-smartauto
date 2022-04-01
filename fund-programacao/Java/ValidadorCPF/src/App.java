import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
            Calc hoho = new Calc();
            
            System.out.println("----------------------------------");
            System.out.println("Informe a operacao desejada"+
                    "\n1 - Validar CPF"+
                    "\n0 - Sair da Aplicacao");        
            System.out.println("----------------------------------");
            int menu = input.nextInt();
            switch (menu) {
                case 1:
                    hoho.cont();
                    //hoho.result();
                    break;
                case 0: 
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opcao inexistente");
                break;
            } 
    }
}
