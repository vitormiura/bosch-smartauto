import java.util.Scanner;

public class Circulo {
    Scanner input = new Scanner(System.in);
    double raio, area, peri;
    
    
    double calcArea (){
        area = 3.14*raio*raio;
        return area;
    }
    double calcPeri (){            
        peri = 2*3.141516*raio;
        return peri;
    }
     
    void result(){
        System.out.println("----------------------------------");
        System.out.println("O círculo de raio: " + raio + "\nArea: " + calcArea() + "\nPerimetro: " + calcPeri());
    }
    void construtor(){   
        System.out.println("Informe do valor do raio do círculo");
        raio = input.nextDouble();
    }
}
