package Entities;

public class Members {
    private int id;
    private String name;
    private int age;
    private String email;

    public Members(int id, String name, int age, String email){
        this.id = id;
        this.name = name;
        this.age = age;
        this.email = email;
    }

    public void display(){
        System.out.println("nome: " + this.name);
        System.out.println("age: " + this.age);
        System.out.println("email: " + this.email);
    }
}

