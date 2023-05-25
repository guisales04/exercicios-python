from abc import ABC, abstractmethod


class Account(ABC):
    _authentication: bool = False

    def __init__(self, agency: int, number_id: int, balance: int) -> None:
        self._agency = agency
        self._number_id = number_id
        self.balance = balance

    def deposit(self, value: int):
        self.balance += value
        print(f"Depositado R${value:.2f}. Saldo atual: R${self.balance:.2f}")

    @abstractmethod
    def withdraw(self, value: int):
        pass


class CC(Account):
    _limite = 1000

    def withdraw(self, value: int):
        if not self._authentication:
            print("Você não está autenticado!")
            return

        if value > self._limite:
            print("Você ultrapassou o limite!")
            return

        if self.balance - value < 0:
            print("Saldo insuficiente!")
            return

        self.balance -= value
        print(f"Retirado R${value:.2f}. Saldo atual: R${self.balance:.2f}")


class CP(Account):
    def withdraw(self, value: int):
        if not self._authentication:
            print("Você não está autenticado!")
            return

        if self.balance - value < 0:
            print("Saldo insuficiente!")
            return

        self.balance -= value
        print(f"Retirado R${value:.2f}. Saldo atual: R${self.balance:.2f}")


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Client(Person):
    def __init__(self, acc: CC | CP, name: str, age: int) -> None:
        super().__init__(name, age)
        self._account = acc

    def withdraw(self, value: int):
        self._account.withdraw(value)


class Bank:
    _clients: list = []

    def __init__(self, agency: int) -> None:
        self._agency = agency

    def add_client(self, client: Client) -> None:
        if client._account._agency != self._agency:
            print('Autenticação falhou!')
            return
        client._account._authentication = True
        self._clients.append(client)


bank = Bank(51)
acc1 = CC(51, 11111, 10000)
c1 = Client(acc1, 'Leonardo', 22)
bank.add_client(c1)
c1.withdraw(1001)
c1.withdraw(1000)
print()

acc2 = CP(51, 22222, 3000)
c2 = Client(acc2, 'Maria', 18)
bank.add_client(c2)
c2.withdraw(3001)
c2.withdraw(2900)
print()

acc3 = CP(52, 33333, 5000)
c3 = Client(acc3, 'João', 19)
bank.add_client(c3)
c3.withdraw(5001)
c3.withdraw(2000)
print()
