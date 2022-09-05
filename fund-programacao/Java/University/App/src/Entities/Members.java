package Entities;

public class Members {
    private String name;
    private int age;
    private String email;

    public Members(String name, int age, String email){
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

