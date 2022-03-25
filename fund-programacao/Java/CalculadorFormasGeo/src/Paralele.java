import java.util.Scanner;

public class Paralele {
    Scanner input = new Scanner(System.in);
    double larg, area, vol, prof, alt;

    double calcArea (){
        area = (2 * larg * prof) + (2 * prof * alt) + (2 * larg * alt);
        return area;
    }
    double calcVol (){
        vol = larg * prof * alt;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("A largura do paralelepipedo: " + larg + "A profundidade: " + prof + "Altura: " + alt + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe a largura do paralelepipedo: ");
        larg = input.nextDouble();
        System.out.println("Informe a profundidade do paralelepipedo: ");
        prof = input.nextDouble();
        System.out.println("Informe a altura do paralelepipedo: ");
        alt = input.nextDouble();
    } 
}
