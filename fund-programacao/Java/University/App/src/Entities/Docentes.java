package Entities;

public class Docentes extends Members{
    private String formacao;

    public Docentes(String name, int age, String email, String formacao){
        super(name, age, email);
        this.formacao = formacao;
    }
}
