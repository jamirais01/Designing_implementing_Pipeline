class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0.0

    def insertCoin(self) -> None:
        self.amount += 1

    def getAmount(self) -> int:
        return self.amount

    def returnCoins(self) -> int:
        returned = self.amount
        self.amount = 0
        return returned
