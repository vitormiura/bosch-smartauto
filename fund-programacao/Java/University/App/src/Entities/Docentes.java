package Entities;

public class Docentes extends Members{
    private String formation;

    public Docentes(int id, String name, int age, String email, String formation){
        super(id, name, age, email);
        this.formation = formation;
    }
}
