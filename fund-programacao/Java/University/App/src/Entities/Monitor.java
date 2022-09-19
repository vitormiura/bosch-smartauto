package Entities;

public class Monitor extends Discentes{
    private double bolsa;
    private boolean aval;
    int Salary = 2000;

    public Monitor(int id, String name, int age, String email, int year, double bolsa, boolean aval, int Salary){
        super(id, name, age, email, year);
        this.bolsa = bolsa;
        this.aval = aval;
        this.Salary = Salary;
    }
}
