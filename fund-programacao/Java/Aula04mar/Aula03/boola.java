package Aula03;

public class boola {
    public static void main(String[] args) throws Exception {
        boolean condicao1 = true;
        boolean condicao2 = 15 < 12;

        System.out.println(condicao1 && !condicao2);
        System.out.println(condicao1 || condicao2);
    }
}