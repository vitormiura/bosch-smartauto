package Entities;

public class Professor extends Docentes{
    int Salary = 7000;

    public Professor(int id, String name, int age, String email, String formation, int Salary){
        super(id, name, age, email, formation);
        this.Salary = Salary;
    }
}
