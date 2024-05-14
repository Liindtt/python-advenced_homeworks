import time
from threading import Thread, Lock
import random


class BankAccount:
    def __init__(self, acc_id: int, name: str, balance: int):
        self.acc_id = acc_id
        self.name = name
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"User {self.name} deposited your balance for {amount} UAH. New balance: {self.balance} UAH.")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"User {self.name} successfully withdrew {amount} UAH from his balance. New balance: {self.balance} UAH.")
                return True
            else:
                print(f"User {self.name} failed to withdraw {amount} UAH from his balance, {self.balance} UAH.")
                return False


class ATM:
    def __init__(self, money: int):
        self.money = money  # К-сть грошей у банкоматі, що доступні для видачі
        self.lock = Lock()

    def atm_replenishment(self, amount: int):
        with self.lock:
            self.money += amount
            print(f"ATM successfully replenished for {amount} UAH. ATM money: {self.money} UAH.")

    def execute_transaction(self, account, amount, transaction_type):
        with self.lock:
            if transaction_type == "withdraw":
                if self.money >= amount and account.withdraw(amount):
                    self.money -= amount
                    print(f"ATM money: {self.money} UAH.")
            elif transaction_type == "deposit":
                account.deposit(amount)


def user_operations(account, atm):
    for _ in range(3):  # Every user doing 3 operations with ATM
        time.sleep(1)  # A break between operations
        operation = random.choice(["withdraw", "deposit"])  # Random operation
        amount = random.randrange(50, 1001, 50)  # Random money amount in operation
        if operation == "withdraw":
            atm.execute_transaction(account, amount, operation)
        elif operation == "deposit":
            atm.execute_transaction(account, amount, operation)


def atm_working(atm_obj):
    while True:
        time.sleep(4)  # A break between replenish of ATM
        amount = random.randrange(1000, 5001, 1000)  # Random amount of replenishment
        atm_obj.atm_replenishment(amount)


accounts = [
    BankAccount(1, "Yaroslav", 10000),
    BankAccount(2, "Alina", 3000),
    BankAccount(3, "Mark", 6000)
]

atm = ATM(20000)

threads = []
for acc in accounts:
    thread = Thread(target=user_operations, args=(acc, atm))
    threads.append(thread)


atm_thread = Thread(target=atm_working, args=(atm, ))
atm_thread.daemon = True
atm_thread.start()

for thread in threads:
    thread.start()
    thread.join()

print("\nFinal balances:")
for account in accounts:
    print(f"User {account.name}: {account.balance} UAH")
print(f"Total money in ATM: {atm.money} UAH")
