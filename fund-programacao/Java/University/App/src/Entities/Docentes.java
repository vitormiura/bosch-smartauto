package Entities;

public class Docentes extends Members{
    private String formation;

    public Docentes(String name, int age, String email, String formation){
        super(name, age, email);
        this.formation = formation;
    }
}
