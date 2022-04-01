import javax.swing.JOptionPane;

public class Calc {
    String cpfString = JOptionPane.showInputDialog("Digite um CPF para ser validado");
    //boolean pass1 = false;
    //boolean pass2 = false; 
    ArrayList<Integer> cpf = new ArrayList<>();
    
    void cont(){
        for (int i = 0; i < cpfString.length(); i++) {
            cpf.add(Integer.parseInt(cpfString.charAt(i) + ""));
        }
        if(cpf.size() == 11){
            int multi = 10;
            double soma = 0;
            for (int num : cpf) {
                soma += num * multi;
                multi -= 1;
                if (multi <= 1) {
                    break;
                }
            }
        }    
    }
}
