package aula01;

public class Main {

    public static void main(String[] args) {
        byte meuByte = 127;
        System.out.printf("Tamanho do byte: %d\n", meuByte);
        short meuShort = 32767;
        System.out.printf("Tamanho do Short: %d\n", meuShort);
        int meuInt = 2_147_483_647;
        System.out.printf("Tamanho do Int: %d\n", meuInt);
        long meuLong = 9_223_372_036_854_775_807L;
        System.out.printf("Tamanho do Long: %d\n", meuLong);
        // Precisão de 6 a 7 digitos.
        float meuFloat = 3.4e+38f;
        System.out.printf("Tamanho do Float: %f\n", meuFloat);
        double meuDouble = 1.7e+308;
        System.out.printf("Tamanho do double: %f\n", meuDouble);
    }
}
