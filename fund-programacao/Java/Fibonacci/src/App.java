import java.util.Arrays;

public class App {

    public static void main(String[] args) {
	    int[] fibonacci = new int[20];
        fibonacci[0] = 0;
        fibonacci[1] = 1;

        for (int i = 2; i < 20; i++) {
            fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];

        }
        System.out.println(Arrays.toString(fibonacci));


    }
}
