package Entities;

public class Discentes extends Members{
    private int year;

    public Discentes(int id, String name, int age, String email, int year) {
        super(id, name, age, email);
        this.year = year;
    }
}
