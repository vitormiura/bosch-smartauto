package DesafioFormasGeo;

import java.util.Scanner;

public class PiramideQuad {
    Scanner input = new Scanner(System.in);
    double area, vol, base, altura, apot; 

    double calcArea (){
        area = (base * base) + ((base/2) * base) + (altura*altura);
        return area;
    }
    double calcVol (){
        vol = ((base * base) * altura) / 3;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("A largura do paralelepipedo: " + larg + "A profundidade: " + prof + "Altura: " + alt + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe a largura do paralelepipedo: ");
         = input.nextDouble();
            
    } 
}
