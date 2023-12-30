# the class name that's the name of your class and can be anything depending on what you are modulling
class Stock:
    # the init method is like a constructor in other languages like java , C++
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # just a simole method and same like a tostring method in java
    def get_discription(self):
        return f"{self.ticker} {self.company} ---- ${self.price}"


# creating an object of the class with stock1,  stock2 and stock3 the objects
stock1 = Stock("Corp", 23.7, "Microsoft")
stock2 = Stock("Inc", 354.7, "Google")
stock3 = Stock("Inc", 234.7, "ZiloTech")


print(stock1.get_discription())
print(stock2.get_discription())
print(stock3.get_discription())
