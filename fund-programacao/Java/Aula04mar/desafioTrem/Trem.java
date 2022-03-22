package desafioTrem;

public class Trem {
    String linha;
    int pos;
    double vel;
    //double acel;
    
    // public Trem(String linha, int pos, double vel){
    //     this.linha = linha;
    //     this.pos = pos;
    //     this.vel = vel;
    //    // this.acel = 0;
    // }

    public void info(){
        System.out.println("------------------------");
        System.out.println("Linha: " + this.linha);
        System.out.println("Posicao:" + this.pos);
        System.out.println("Velocidade" + this.vel);
        System.out.println("------------------------");
    }

    // public void percorrer(int tempo){
    //     this.pos += this.vel * tempo;
    // }

    // public void acelerar(int tempo){
    //     this.vel += this.acel * tempo;
    // }


}