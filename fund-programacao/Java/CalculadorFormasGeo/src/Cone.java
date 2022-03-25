import java.util.Scanner;

public class Cone {
    Scanner input = new Scanner(System.in);
    double raio, area, vol, alt, geratriz;

    double calcArea (){
        area = 3.14 * raio * (geratriz + raio);
        return area;
    }
    double calcVol (){
        vol = (3.14 * (raio * raio) * alt) / 3;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("O cilindro de cone: " + raio + "Altura: " + alt + "Altura: " + geratriz + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe o raio do cone: ");
        raio = input.nextDouble();
        System.out.println("Informe a altura do cone: ");
        alt = input.nextDouble();
        System.out.println("Informe a geratriz do cone: ");
        geratriz = input.nextDouble();
    } 
}
