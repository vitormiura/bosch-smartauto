package Entities;

public class Disciplinas {
    private int id;
    private String name;
    private int alunos;
    private int professor;
    private int monitor;

    public Disciplinas(int id, String name, int alunos, int professor, int monitor){
        this.id = id;
        this.name = name;
        this.alunos = alunos;
        this.professor = professor;
        this.monitor = monitor;
    }

    public void print(){
        System.out.println(this.name);
    }
}
