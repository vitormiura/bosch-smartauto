package heranca;

public class App {
    public static void main(String[] args) throws Exception {
        Compra compra1 = new Compra();
        compra1.cliente = "Joao Jose";
        compra1.adicionarItem(new Item("notebook", 1, 5000));
        compra1.adicionarItem(new Item("iphone", 2,6000));
        compra1.adicionarItem(new Item("Amazon Echo", 2, 2000));
        System.out.println(compra1.itens.size());
        System.out.println(compra1.obterValorTotal());
    }
}
