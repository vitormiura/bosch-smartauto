package Entities;

import java.util.ArrayList;

public class Students extends Discentes {
    private double media;
    ArrayList<Double> provas = new ArrayList<Double>();
    private int faltas;
    private boolean status;

    public Students(int id, String name, int age, String email, int year, double media, ArrayList<Double> provas, int faltas, boolean status){
        super(id, name, age, email, year);
        this.provas = provas;
        this.faltas = faltas;
        this.status = status;
    }
}
