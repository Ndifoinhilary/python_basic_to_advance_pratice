from abc import ABC, abstractmethod


class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_discription(self):
        return f"{self.price}"


class Stock(Asset):
    def __init__(self, price, ticker, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def get_discription(self):
        return f"{self.ticker} {self.company} ---- ${self.price}"


class Bond(Asset):
    def __init__(self, price, description, duration, yeild):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yeild = yeild

    def get_discription(self):
        return f"{self.description} {self.duration} ---- ${self.price} and a yield of {self.yeild} "


bond = Bond(12, "Learning OOP in python", "1h", "Very productive")

print(bond.get_discription())
