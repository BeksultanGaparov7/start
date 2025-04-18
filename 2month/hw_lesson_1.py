class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнить счёт на указанную сумму"""
        if amount > 0:
            self.balance += amount
            print(f"Счёт пополнен на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма для пополнения должна быть положительной")

    def withdraw(self, amount):
        """Снять деньги со счёта, если достаточно средств"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снято {amount}. Текущий баланс: {self.balance}")
            else:
                print("Недостаточно средств на счете")
        else:
            print("Сумма для снятия должна быть положительной")

    def show_balance(self):
        """Показать текущий баланс"""
        print(f"Текущий баланс счёта {self.owner}: {self.balance}")



if __name__ == "__main__":
    account = BankAccount("Иван Иванов", 1000)

    account.show_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
    account.withdraw(-10)
    account.show_balance()
