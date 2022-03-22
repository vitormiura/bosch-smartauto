package DesafioFormasGeo;

import java.util.Scanner;

public class Cubo {
    Scanner input = new Scanner(System.in);
    double aresta, area, vol;

    double calcArea (){
        area = (aresta*aresta)*6;
        return area;
    }
    double calcVol (){
        vol = aresta * aresta * aresta;
        return vol;
    }
    void result(){
        System.out.println("----------------------------------");   
        System.out.println("O cubo de aresta: " + aresta + "\nArea: " + calcArea() + "\nVolume: " + calcVol());
    }
    void construtor(){   
        System.out.println("Informe a aresta de um cubo: ");
        aresta = input.nextDouble();
    } 
}
