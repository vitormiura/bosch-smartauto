package heranca2;

public class Main {
    public static void main(String[]args){
        Aluno aluno1 = new Aluno("joao");
        Aluno aluno2 = new Aluno("Maria");
        Aluno aluno3 = new Aluno("dante");

        Curso curso1 = new Curso("java");
        Curso curso2 = new Curso("Python");
        Curso curso3 = new Curso("VsDiA");

        curso1.adicionarAluno(aluno1);
        curso1.adicionarAluno(aluno2);
        curso2.adicionarAluno(aluno1);
        curso2.adicionarAluno(aluno3);
        aluno1.adicionarCurso(curso3);
        aluno2.adicionarCurso(curso3);
        aluno3.adicionarCurso(curso3);

        System.out.println(cursos3.obterPorCurso());
    }
}
