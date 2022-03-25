import java.util.Scanner;

public class PiramideQuad {
    Scanner input = new Scanner(System.in);
    double area, vol, base, altura, hip, areaBase, at; 

    double calcArea (){
        areaBase = base * base;
        hip = Math.sqrt(((base / 2) * (base / 2)) + (altura * altura));
        at = (base * hip) / 2;
        area = (at * 4) + areaBase;
        return area;
    }
    double calcVol (){
        vol = (areaBase * altura) / 3;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("Altura: " + altura + "\nBase: " + base + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe a base da piramide de base quadrada: ");
        base = input.nextDouble();
        System.out.println("Informe a altura da piramide de base quadrada: ");
        altura = input.nextDouble();
    } 
}
