package Entities;

public class Discentes extends Members{
    private int year;

    public Discentes(String name, int age, String email, int year) {
        super(name, age, email);
        this.year = year;
    }
}
