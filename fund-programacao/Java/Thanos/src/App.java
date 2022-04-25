import java.util.ArrayList;
import java.util.Random;

public class App {

    public static void main(String[] args) {
        ArrayList<String> vetor = new ArrayList<>();
        vetor.add("Breno");
        vetor.add("Vitor");
        vetor.add("Icaro");
        vetor.add("Nathan");
        vetor.add("Dante");
        vetor.add("Leo");
        vetor.add("Abe");
        vetor.add("Vini");
        vetor.add("Josoaldo");

        int x = vetor.size();

        if (x % 2 == 0) {
            x = x / 2;
        } else {
            x = x / 2 + 1;
        }
        // Iae lindão
        // se é padeiro?
        // e esse pãozinho ae?
        Random gerador = new Random();
        for (int i = 0; i < x; i++) {

            vetor.remove(gerador.nextInt(vetor.size()));
        }
        for (int i = 0; i < vetor.size(); i++) {
            System.out.println(vetor.get(i));
        }
    }
}
