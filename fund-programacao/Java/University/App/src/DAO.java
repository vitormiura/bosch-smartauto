import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import Entities.Students;

public class DAO {
    public static Connection connect() throws SQLException {
        String url = "jdbc:postgresql://db.tapnomaqtntnlkpcwvwv.supabase.co:5432/postgres?user=postgres&password=miuravitor123!";
        return DriverManager.getConnection(url);
    }

    public void insert(Connection connection) throws SQLException {
        Statement statement = connection.createStatement();
        statement.executeQuery(
                "INSERT INTO disciplina (nome, alunos, professor, monitor) VALUES ('dante viado', 1 , 1, 1)");
    }
}
