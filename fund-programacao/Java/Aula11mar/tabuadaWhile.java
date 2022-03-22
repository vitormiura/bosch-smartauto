
public class tabuadaWhile {
    public static void main(String[] args) throws Exception {
        int count = 1;
        int mult[] = {1,2,3,4,5,6,7,8,9,10};
        
            System.out.println("-------------------------------");
        while (count <= 10 ) {
            System.out.println(mult + " x " + count + " = " + count * mult);
            count++;
        }
    }
}
