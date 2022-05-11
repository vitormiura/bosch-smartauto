public class tabuadaFor {
    public static void main(String[] args) throws Exception {
        int i=1;
        int j=1;

        System.out.println("Tabuadas de 1 a 10");

        for (i=1;i<=10;i++){
            for (j=1; j<=10; j++){
                System.out.println(i + "x" + j + "=" + (i*j));
            }
        }
    }
}
