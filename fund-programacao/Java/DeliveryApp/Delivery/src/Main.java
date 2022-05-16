import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        while(true){
            try{
                Scanner input = new Scanner(System.in);

                    System.out.println("----------------------------------");
                        System.out.println("Delivery"+
                        "\n1-Cadastrar Restaurante"+
                        "\n2-Cadastrar usuário"+
                        "\n3-Efetuar Pedido"+ // SUBMENU PARA A ESCOLHA DO RESTAURANTE
                        "\n0 - Sair da Aplicacao");
                        int menu = input.nextInt();
                        System.out.println("----------------------------------");

                        switch (menu) {
                            case 1:
                                
                                break;
                            case 2: 
                                
                                break;
                            case 3: 
                                
                                break;
                            case 0: 
                                System.exit(0);
                                break;
                            default:
                                System.out.println("Opcao inexistente...");
                            break;
                        }
            }catch (NumberFormatException e) {
                System.out.println("Apenas numeros sao aceitos...");}
        }
    }
}
