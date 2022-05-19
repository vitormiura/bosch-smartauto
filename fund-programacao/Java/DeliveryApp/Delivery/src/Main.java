import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Methods func = new Methods();
        String tempUser = "";
        boolean autenticado = false;
        boolean main = false;
        while(autenticado == false){

            Scanner input = new Scanner(System.in);
            System.out.println("----------------------------------");
                System.out.println("LOGIN"+
                "\n1 - Entrar"+
                "\n2 - Cadastrar usuário"+
                "\n0 - Sair da Aplicacao");
                int menu = input.nextInt();
                System.out.println("----------------------------------");

                switch (menu) {
                    case 1:
                        System.out.println("Seu usuario: ");
                        String username = input.nextLine();
                        if(func.userAuth(username)){
                            autenticado = true;
                            main = true;
                            tempUser = username;
                        }else{
                            System.out.println("Usuario n encontrado!");
                        }
                        break;
                    case 2: 
                        System.out.println("Entre seu nome: ");
                        String a1 = input.nextLine();
                        System.out.println("Entre seu endereco: ");
                        String a2 = input.nextLine();
                        System.out.println("Entre seu CPF: ");
                        String a3 = input.nextLine();
                        func.addUser(new Usuario(a1, a2, a3));
                        break;
                    case 0: 
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Opcao inexistente...");
                    break;
                }
        while(main){
            Scanner input2 = new Scanner(System.in);
            System.out.println("----------------------------------");
                System.out.println("Bem vindo ao delivery brabao"+
                "\n1-Fazer pedido"+
                "\n2-Listar pedidos"+
                "\n3-Restaurantes abertos"+
                "\n4-Abrir um novo restaurante"+
                "\n5-Editar cardapio restaurantes abertos"+
                "\n6-Excluir restaurante"+
                "\n0 - Sair da Aplicacao");
                int menu2 = input2.nextInt();
                System.out.println("----------------------------------");

                switch (menu2){
                    case 1:
                        func.makeOrder(input, tempUser);
                        break;
                    case 2:
                        func.listOrder(tempUser);
                        break;
                    case 3:
                        System.out.println(func.printRest());
                        break;
                    case 4:
                        System.out.println("Digite o nome do restaurante: ");
                        String a1 = input.nextLine();
                        System.out.println("Digite o CNPJ: ");
                        String a2 = input.nextLine();
                        System.out.println("Digite a localizacao: ");
                        String a3 = input.nextLine();
                        func.addRest(new Restaurante(a1, a2, a3));
                        break;
                    case 5:
                        //faze essa bosta dps, mt trampo 
                        break;
                    case 6:
                        func.remoRest(input);
                        break;
                    case 0:
                        System.exit(0);
                        break;
                }
            }
        }
    }
}
