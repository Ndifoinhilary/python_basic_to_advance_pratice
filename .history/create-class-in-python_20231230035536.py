


class Stock:
    def __init__(self , ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    
    def get_discription(self):
        return f'{self.ticker} {self.company} ---- ${self.price}'





stock1 = Stock("Corp", 23.7, "Microsoft")
stock2 = Stock("Inc", 354.7, "Google")
stock3 = Stock("Inc", 234.7, "ZiloTech")


print(stock1.get_discription())
print(stock2.get_discription())
print(stock3.get_discription())