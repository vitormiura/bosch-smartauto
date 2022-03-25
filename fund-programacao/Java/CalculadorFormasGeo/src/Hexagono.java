import java.util.Scanner;

public class Hexagono {

    Scanner input = new Scanner(System.in);
    double lado, peri, area;
    double calcArea(){
        area = (((lado*lado) * 1.7) / 4) * 6; 
        return area;
    }

    double calcPeri(){
        peri = lado*6;
        return peri;
    }
    void result(){
        System.out.println("----------------------------------");
        System.out.println("O Hexagono de lado: " + lado + "\nArea: " + calcArea() + "\nPerimetro: " + calcPeri());
    }
    void construtor(){
        System.out.println("Informe do valor do lado do hexagono regular: ");
        lado = input.nextDouble();
    }
}
