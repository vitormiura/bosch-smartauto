import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DAO {
    public Connection DBconnect(){
        Connection con = null;
        try{
            String url = "jdbc:postgresql://clpuectczmwtno:57620ac3a3eeb990ce187fd1f1751c21db4d57f7d8758f3f38a19a474a9251d4@ec2-34-234-240-121.compute-1.amazonaws.com:5432/deu7o7mk1t1if";
            con = DriverManager.getConnection(url);
        } catch (SQLException error){
            System.err.println(error.getMessage());
        }
        return con;
    }
}
