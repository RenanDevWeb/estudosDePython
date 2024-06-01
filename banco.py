
class Conta:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.saque = 0

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f"Depósito de R${quantia:.2f} realizado com sucesso.")
        else:
            print("A quantia para depósito deve ser positiva.")

    def sacar(self, quantia):
        if self.saque <=2:
            if quantia > 0:
                if quantia <= self.saldo:
                    self.saldo -= quantia
                    self.saque += 1
                    print(self.saque)
                    print(f"Saque de R${quantia:.2f} realizado com sucesso.")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("A quantia para saque deve ser positiva.")
        else:
            print(f"O limite de saque {self.saque} foi atingido")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta1 = Conta("João Silva", 500.0)
conta1.verificar_saldo()
conta1.depositar(1500.0)
conta1.sacar(200.0)
conta1.sacar(200.0)
conta1.sacar(200.0)
conta1.sacar(50.0)
conta1.sacar(50.0)

conta1.verificar_saldo()

