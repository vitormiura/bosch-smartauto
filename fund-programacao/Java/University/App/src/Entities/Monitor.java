package Entities;

public class Monitor extends Discentes{
    private double bolsa;
    private boolean aval;

    public Monitor(String name, int age, String email, int year, double bolsa, boolean aval){
        super(name, age, email, year);
        this.bolsa = bolsa;
        this.aval = aval;
    }
}
