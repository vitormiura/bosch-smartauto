package Entities;

public class Professor extends Docentes{
    int Salary = 7000;

    public Professor(String name, int age, String email, String formation, int Salary){
        super(name, age, email, formation);
        this.Salary = Salary;
    }
}
