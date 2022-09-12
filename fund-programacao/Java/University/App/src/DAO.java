import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DAO {
    public Connection DBconnect() throws SQLException{
        Connection con = null;
        try{
            String url = "jdbc:mysql://127.0.0.1:3306/universidade?user=root&password=";
            con = DriverManager.getConnection(url);
        } catch (SQLException error){
            System.err.println(error.getMessage());
        }
        return con;
    }
}
