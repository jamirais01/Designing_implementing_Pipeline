from bank_account import BankAccount

def main():
    print("Program starting.")
    print("Welcome to the bank account program.\n")

    account = BankAccount()

    while True:
        print("1 - Deposit money")
        print("2 - Withdraw money")
        print("3 - Show balance")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Money deposited.\n")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            success = account.withdraw(amount)

            if success:
                print("Money withdrawn.\n")
            else:
                print("Not enough balance.\n")

        elif choice == "3":
            print(f"Current balance: {account.getBalance()}€\n")

        elif choice == "0":
            print("Program ending.")
            break

if __name__ == "__main__":
    main()
