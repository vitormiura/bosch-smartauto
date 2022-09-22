import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import Entities.Students;
import Entities.Disciplinas;

public class DAO {
    public static Connection connect() throws SQLException {
        String url = "jdbc:postgresql://db.tapnomaqtntnlkpcwvwv.supabase.co:5432/postgres?user=postgres&password=miuravitor123!";
        return DriverManager.getConnection(url);
    }


    public ArrayList<Disciplinas> get(Connection connection) throws SQLException {
        Statement statement = connection.createStatement();
        ResultSet rs = statement.executeQuery("SELECT * FROM disciplina");
        
        ArrayList<Disciplinas> disc = new ArrayList<>();
        
        while (rs.next()) {
            // System.out.println(rs.getString(1));
            Disciplinas disciplinas = new Disciplinas(
                rs.getInt(1), 
                rs.getString(2), 
                rs.getInt(3), 
                rs.getInt(4), 
                rs.getInt(5)
            );
            disc.add(disciplinas);
        }
        return disc;
    }

    public void insert(Connection connection) throws SQLException {
        Statement statement = connection.createStatement();
        statement.executeQuery(
                "INSERT INTO disciplina (nome, alunos, professor, monitor) VALUES ('bolet', 1 , 1, 1)");
    }
}
