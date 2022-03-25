import java.util.*;

public class Main {
   public static void main(String[] args) {
        while(true){
            try{    
                Scanner input = new Scanner(System.in);
                    Quadrado quad = new Quadrado();
                    Retangulo ret = new Retangulo();
                    Circulo cir = new Circulo();
                    Hexagono hex = new Hexagono();
                    TrianguloEqui tri = new TrianguloEqui();
                    Cubo cubo = new Cubo();
                    Esfera esf = new Esfera();
                    Cilindro cil = new Cilindro();
                    Cone cone = new Cone();
                    Paralele para = new Paralele();
                    PiramideQuad pira = new PiramideQuad();

                    System.out.println("----------------------------------");
                    System.out.println("Informe a operacao desejada"+
                    "\n1-Quadrado"+
                    "\n2-Circulo"+
                    "\n3-Triangulo Equilatero"+
                    "\n4-Hexagono Regular" +
                    "\n5-Retangulo" +
                    "\n6-Cubo" +
                    "\n7-Esfera" +
                    "\n8-Cilindro" +
                    "\n9-Cone" +
                    "\n10-Paralelepipedo" +
                    "\n11-Piramide de base quadrada" +
                    "\n0 - Sair da Aplicacao");
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
                            cubo.construtor();
                            cubo.result();
                            break;
                        case 7: 
                            esf.construtor();
                            esf.result();
                            break;
                        case 8: 
                            cil.construtor();
                            cil.result();
                            break;
                        case 9: 
                            cone.construtor();
                            cone.result();
                            break;
                        case 10: 
                            para.construtor();
                            para.result();
                            break;
                        case 11:
                            pira.construtor();
                            pira.result();
                            break;
                        case 0: 
                            System.exit(0);
                            break;
                        default:
                            System.out.println("opcao inexistente");
                        break;
                    }   
                }catch (NumberFormatException e) {
                    System.out.println("Apenas numeros sao aceitos...");  
            }
        }
    }
}