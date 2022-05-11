import java.util.Scanner;

public class tabuadaWhile {
    public static void main(String[] args) throws Exception {
        int userNum;
        int mult = 0;
        int total = 0;
    
    
        Scanner input = new Scanner(System.in);
        System.out.println("Informe um número: ");
        userNum = input.nextInt();
    
        for (int x = 0; x < 10; x++) {
            total = userNum * ++mult;
            System.out.println(userNum + " x " + mult + " = " + total);
        }
    }
}
