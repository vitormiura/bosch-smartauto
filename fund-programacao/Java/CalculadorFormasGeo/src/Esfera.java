import java.util.Scanner;

public class Esfera {
    Scanner input = new Scanner(System.in);
    double raio, area, vol;

    double calcArea (){
        area = 4 * 3.14 * (raio * raio);
        return area;
    }
    double calcVol (){
        vol = (4 * 3.14 * (raio * raio * raio)) / 3;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("A esfera de raio: " + raio + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe o raio de uma esfera: ");
        raio = input.nextDouble();
    } 
}
