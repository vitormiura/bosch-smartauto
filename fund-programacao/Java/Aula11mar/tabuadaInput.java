import java.util.Scanner;

public class tabuadaInput {
    public static void main(String[] args) throws Exception {
        int num;

        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Digite o numero: ");
            num = input.nextInt();
        }
        if(num >= 0){
            for (int i = 0; i < 11; i++){
                int tabu = num * i;
                System.out.println(num + " x " + i + " = " + tabu );
            }
        }
    }
}

