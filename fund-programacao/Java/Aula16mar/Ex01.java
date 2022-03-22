import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) throws Exception {

        Scanner input = new Scanner(System.in);
        String num = "";
        boolean cond1, cond2;

        try {

            while (true) {

                System.out.println("Digite um numero para ver se ele e primo ou digite sair para sair: ");
                num = input.nextLine();
                input.close();

                if (num.equalsIgnoreCase("sair")) {
                    break;
                }
                cond1 = Integer.parseInt(num) == 1 || Integer.parseInt(num) % 2 == 0 || Integer.parseInt(num) % 3 == 0
                        || Integer.parseInt(num) % 5 == 0 || Integer.parseInt(num) % 7 == 0;
                cond2 = Integer.parseInt(num) == 2 || Integer.parseInt(num) == 3 || Integer.parseInt(num) == 5
                        || Integer.parseInt(num) == 7;

                if (cond2 == true) {
                    System.out.println("O numero " + num + " é primo");
                } else {
                    if (cond1 == true) {
                        System.out.println("O numero " + num + " nao é primo");
                    } else {
                        System.out.println("O numero " + num + " é primo");
                    }
                }
            }
        } catch (NumberFormatException e) {
            System.out.println("Apenas numeros...");
        }
    }
}
