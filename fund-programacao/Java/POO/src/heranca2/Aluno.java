package heranca2;

import java.util.ArrayList;

public class Aluno {
    String nome;
    ArrayList<Cursos> cursos = new ArrayList<>();

    Aluno(String nome){
        this.nome = nome;
    }
    void adicionarCurso(Cursos cursos){
        this.cursos.add(cursos);
        cursos.alunos.add(this);
    }
}
