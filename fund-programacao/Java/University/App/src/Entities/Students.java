package Entities;

import java.util.ArrayList;

public class Students extends Discentes {
    private double media;
    ArrayList<Double> provas = new ArrayList<Double>();
    private int faltas;
    private boolean status;

    public Students(String name, int age, String email, int year, double media, ArrayList<Double> provas, int faltas, boolean status){
        super(name, age, email, year);
        this.provas = provas;
        this.faltas = faltas;
        this.status = status;
    }
}
