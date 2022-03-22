package DesafioFormasGeo;

import java.util.*;

public class Main {
   public static void main(String[] args) {
        try{
            while(true){
                Scanner input = new Scanner(System.in);

                Quadrado quad = new Quadrado();
                Retangulo ret = new Retangulo();
                Circulo cir = new Circulo();
                Hexagono hex = new Hexagono();
                TrianguloEqui tri = new TrianguloEqui();

                System.out.println("----------------------------------");
                System.out.println("Informe a operaçao desejada"+
                "\n1-Quadrado"+
                "\n2-Circulo"+
                "\n3-Triangulo Equilatero"+
                "\n4-Hexagono Regular" +
                "\n5-Retangulo" +
                "\n6-Cubo" +
                "\n7-Esfera" +
                "\n8-Cilíndro" +
                "\n9-Cone" +
                "\n10-Paralelepipedo" +
                "\n11-Pirâmide de base quadrada");
                int menu = input.nextInt();
                System.out.println("----------------------------------");
                
                switch (menu) {
                    case 1:
                        quad.construtor();
                        quad.result();
                        break;
                    case 2:
                        cir.construtor();
                        cir.result();
                        break;
                    case 3: 
                        tri.construtor();
                        tri.result();
                        break;
                    case 4: 
                        hex.construtor();
                        hex.result();
                        break;
                    case 5: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 6: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 7: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 8: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 9: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 10: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 11: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 12: 
                        ret.construtor();
                        ret.result();
                        break;
                    case 13: 
                        break;
                    default:
                        System.out.println("opçao inexistente");
                    break;
                }
            }
        }catch (NumberFormatException e) {
        System.out.println("Apenas numeros são aceitos...");    
    }   
}
}
