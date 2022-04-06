import static java.lang.Math.toIntExact;
import java.util.Scanner;

public class Calc {

    long cpf, resto, num = 10000000000L;
    int j = 0, i = 0, d1 = 0, d2 = 2;
    int[] valid = new int[11];

    Scanner input = new Scanner(System.in);   

    void result(){
        for (j=0;j<11;j++){        
            resto= (cpf % num);
            i= toIntExact(cpf / num);
             num=num/10;
            cpf=resto;         
            valid[j]=i;     
        }
        i=11;        
        for (j=0;j<10;j++){            
            d2=d2+(valid[j]*i);           
            i=i-1;
        }
        d1= d1 * 10 % 11; 
        d2= d2 * 10 % 11;    
        if (d1==valid[9] && (d2==valid[10])){
            System.out.println("O "+ input +" é um CPF válido");
        }else{
            System.out.println("O "+ input + "é um CPF inválido");  
        }
    }
    void inputi(){   
        System.out.println("Informe o CPF desejado: ");
        cpf = input.nextLong();
    }
}
