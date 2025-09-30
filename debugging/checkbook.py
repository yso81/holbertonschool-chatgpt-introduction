class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
        action = input("Enter the number of your choice: ")
        if action == '4' or action.lower() == 'exit':
            break
        elif action == '1' or action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == '2' or action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == '3' or action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()