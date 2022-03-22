package DesafioFormasGeo;

import java.util.Scanner;

public class Retangulo {
    Scanner input = new Scanner(System.in);
    double comprimento, largura, area, peri;
    
    double calcArea (){
        area = comprimento*largura;
        return area;
    }
     double calcPeri (){
        peri = (2*comprimento)+(2*largura);
        return peri;
    }
     
    void result(){
        System.out.println("----------------------------------");
        System.out.println("O retangulo de largura: " + largura + "\nComprimento: " + comprimento + "\nArea: " + calcArea() + "\nPerimetro: " + calcPeri());
    }
    void construtor(){
        System.out.println("Informe do valor do comprimento do retângulo");
        comprimento = input.nextDouble();
        System.out.println("Informe do valor da largura do retângulo");
        largura = input.nextDouble();
    }
}
