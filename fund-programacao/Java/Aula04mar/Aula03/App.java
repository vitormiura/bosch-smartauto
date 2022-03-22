package Aula03;

public class App {
    public static void main(String[] args) throws Exception {
        String minhaString = "Like a Bosch";
        System.out.println(minhaString + "!");
        System.out.println(minhaString.concat("!!!"));

        minhaString=minhaString.concat("!!");
        System.out.println(minhaString);

        System.out.println(minhaString.charAt(0)); //retorna apenas pos 0.
        System.out.println(minhaString.startsWith("Like"));
        System.out.println(minhaString.endsWith("h"));
        System.out.println(minhaString.toUpperCase());
        System.out.println(minhaString.toLowerCase());
    }
}
