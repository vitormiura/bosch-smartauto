package DesafioFormasGeo;

import java.util.Scanner;

public class Cilindro {
    Scanner input = new Scanner(System.in);
    double raio, area, vol, alt;

    double calcArea (){
        area = 2 * (3.14 * (raio * raio)) + 2 * (raio * 3.14 * alt);
        return area;
    }
    double calcVol (){
        vol = 3.14 * (raio * raio) * alt;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("O cilindro de raio: " + raio + "Altura: " + alt + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe o raio do cilindro: ");
        raio = input.nextDouble();
        System.out.println("Informe a altura do cirilo: ");
        alt = input.nextDouble();
    } 
}
