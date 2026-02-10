class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0.0

    def insertCoin(self, value: float) -> None:
        self.amount += 1
        self.value += value

    def getStatus(self) -> tuple[int, float]:
        return self.amount, self.value

    def returnCoins(self) -> tuple[int, float]:
        returned_amount = self.amount
        returned_value = self.value
        self.amount = 0
        self.value = 0.0
        return returned_amount, returned_value
