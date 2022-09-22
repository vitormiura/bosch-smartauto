import java.sql.Connection;
import java.util.ArrayList;

import Entities.Disciplinas;

public class App {
    public static void main(String[] args) throws Exception {
        DAO makako = new DAO();
        Connection connection = DAO.connect();
        // makako.insert(connection);

        ArrayList<Entities.Disciplinas> disciplinas = makako.get(connection);

        for (Disciplinas disciplinas2 : disciplinas) {
            disciplinas2.print();
        }   
    }
}
