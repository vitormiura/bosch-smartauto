package DesafioFormasGeo;

import java.util.Scanner;

public class Quadrado {
    Scanner input = new Scanner(System.in);
    double lado, area, peri;
    double calcArea (){
        area = lado*lado;
        return area;
    }
     double calcPeri (){
        peri = 4*lado;   
        return peri;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("O quadrado de lado: " + lado + "\nArea: " + calcArea() + "\nPerimetro: " + calcPeri());
    }
    void construtor(){   
        System.out.println("Informe do valor do lado do quadrado");
        lado = input.nextDouble();
    } 
}
