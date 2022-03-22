package desafioTrem;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Colisao de Trens!");
        Scanner input = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.##");
        double tempo = 0;
        double posFinal = 0;
        Trem tremA = new Trem();

        System.out.println("Digite a linha: ");
        tremA.linha = input.nextLine();
        System.out.println("Digite a posicao: ");
        tremA.pos = input.nextInt();
        System.out.println("Digite a velocidade em KM/H: ");
        tremA.vel = input.nextDouble();

        input.nextLine();
        Trem tremB = new Trem();

        System.out.println("Digite a linha: ");
        tremB.linha = input.nextLine();
        System.out.println("Digite a posicao: ");
        tremB.pos = input.nextInt();
        System.out.println("Digite a velocidade em KM/H: ");
        tremB.vel = input.nextDouble()*-1;
        if (tremA.pos < tremB.pos){
            tremA.vel = tremB.vel *-1;
        }else{
            tempo = (tremA.pos - tremB.pos)/(tremA.vel - tremB.vel);
            posFinal = (tremA.pos - (tremA.vel * tempo));
            System.out.println("O trem após " + df.format((tempo * 3600)) + " segundos" + " no km " + df.format(posFinal));
        }if (tempo == 0){
            System.out.println("O trem bateu");
        }
        
        tremA.info();
        tremB.info();

        input.close();
    }
}