package DesafioFormasGeo;

import java.util.Scanner;

public class TrianguloEqui {
    Scanner input = new Scanner(System.in);
    double base, area, peri, altura;
    double calcArea(){
        area = (base * altura) / 2; 
        return area;
    }
    double calcPeri(){
        peri = base*3;
        return peri;
    }
    void result(){
        System.out.println("----------------------------------");
        System.out.println("O triangulo equi. de base: " + base + "\nAltura: " + altura + "\nArea: " + calcArea() + "\nPerimetro: " + calcPeri());
    }
    void construtor(){
        System.out.println("Informe do valor da base do triangulo equi.");
        base = input.nextDouble();
        System.out.println("Informe do valor da altura do triangulo equi.");
        altura = input.nextDouble();
    }
}
