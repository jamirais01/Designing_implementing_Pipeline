from coin_acceptor import CoinAcceptor

def main():
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")

    acceptor = CoinAcceptor()

    while True:
        value = float(input("Insert coin(0 return, -1 exit): "))

        if value == -1:
            print("Exiting program.\n")
            break

        if value == 0:
            print("Returning coins...")
            amount, total = acceptor.returnCoins()
            print(f"{amount} coins with {total}€ value returned.")
            amount, total = acceptor.getStatus()
            print(f"Inserted coins = {amount}, value = {total}€\n")
        else:
            print("Inserting...")
            acceptor.insertCoin(value)
            amount, total = acceptor.getStatus()
            print(f"Inserted coins = {amount}, value = {total}€\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
