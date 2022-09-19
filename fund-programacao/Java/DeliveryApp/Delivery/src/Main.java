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
                "\n2 - Cadastrar usuario"+
                "\n0 - Sair da Aplicacao");
                int menu = input.nextInt();
                System.out.println("----------------------------------");

                switch (menu) {
                    case 1:
                        System.out.println("Digite seu usuario: ");
                        String username = input.next();
                        if(func.userAuth(username)){
                            autenticado = true;
                            main = true;
                            tempUser = username;
                        }else{
                            System.out.println("Usuario n encontrado!");}
                        break;
                    case 2: 
                        System.out.println("Entre seu nome: ");
                        String a1 = input.next();
                        System.out.println("Seu endereco: ");
                        String a2 = input.next();
                        System.out.println("Entre seu CPF: ");
                        String a3 = input.next();
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
                System.out.println("Seja bem vindo, "+ tempUser +
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
                    func.makeOrder(input2, tempUser);
                    break;
                case 2:
                    func.listOrder(tempUser);
                    break;
                case 3:
                    System.out.println(func.printRest());
                    break;
                case 4:
                    System.out.println("Digite o nome do restaurante: ");
                    String a1 = input2.next();
                    System.out.println("Digite o CNPJ: ");
                    String a2 = input2.next();
                    System.out.println("Digite a localizacao: ");
                    String a3 = input2.next();
                    func.addRest(new Restaurante(a1, a2, a3));
                    break;
                case 5:
                    Scanner input3 = new Scanner(System.in);
                    int ind = func.restSelect(input3);
                    if (ind != -1) {
                        boolean loop2 = true;
                    while(loop2){
                    System.out.println("----------------------------------");
                    System.out.println("(" + func.printRest().get(ind) + ") " + "- Gerenciador" +
                        "\n1-Imprimir cardapio do restaurante"+
                        "\n2-Adicionar lanche"+
                        "\n3-Remover lanche"+
                        "\n4-Retornar ao menu"+
                        "\n0 - Sair da Aplicacao");
                    int menu3 = input3.nextInt();
                    System.out.println("----------------------------------");     
                    switch (menu3){
                        case 1:
                            func.printCardRest(input3, ind);
                            break;
                        case 2:
                            System.out.println("Nome do lanche que desejas adicionar: ");
                            String nlanche = input3.next();
                            System.out.println("Preco do " + nlanche + ": ");
                            double planche = input3.nextDouble();
                            func.addItemRest(new Lanche(nlanche, planche), ind); 
                            //func.adicionarItemsRestaurante(new Lanche(nlanche, planche), ind); 
                            break;
                        case 3:
                            func.rmvItemRest(input3, ind);
                            break;
                        case 4:
                            loop2 = false;
                            break;
                        default:
                            System.out.println("Aconteceu algum erro");
                            break;
                        }
                    }
                }        
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