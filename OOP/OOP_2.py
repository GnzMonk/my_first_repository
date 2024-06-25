class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("WARNING!")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.__balance}"

def main():
    savings = BankAccount(100)
    print(savings.get_balance())

    print(savings)

if __name__ == "__main__":
    main()