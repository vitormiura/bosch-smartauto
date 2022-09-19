import java.sql.Connection;

public class App {
    public static void main(String[] args) throws Exception {
        DAO makako = new DAO();
        Connection connection = DAO.connect();
        makako.insert(connection);

    }
}
