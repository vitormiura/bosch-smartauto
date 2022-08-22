package Bosch;

public class Conta {
    double saldo;

    void deposito(double valor){
        this.saldo = this.saldo + valor;
    }

    void deposito(double valor, String texto){
        this.saldo += this.saldo + valor;
    }
}
