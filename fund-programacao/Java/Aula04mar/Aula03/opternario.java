package Aula03;

public class opternario {

    public static void main(String[] args) throws Exception {
    // String resultado;
    // double media = 4.9;
    // resultado = media >= 5 ? "Aprovado" : "Reprovado";
    // System.out.println(resultado);
        
    double media = 7.1;
    int faltas = 20;
    boolean postura = true;

    if(media>=5.0 && faltas<25 && postura==true)
        System.out.println("Aprovado");
    else if(media < 5.0 && faltas < 25 && postura)
        System.out.println("Rec");
    else if(media >= 5.0 && faltas >= 25 && postura)
        System.out.println("Sem férias!");
    else if(media > 5.0 && faltas < 25 && !postura)
        System.out.println("Chamar para conversar");
    else
        System.out.println("Reprovado!");
    

    }
}