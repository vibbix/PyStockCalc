from typing import List


# Stock class, holds the stock ticker name and
class Stock(object):
    def __init__(self):
        self.symbol = ""
        self.own = 0

    def __init__(self, symbol: str, own: int):
        self.symbol = symbol
        self.own = own


# Portfolio class
class Portfolio(object):
    def __init__(self):
        self.name = str
        self.stocks = List[Stock]

    def __init__(self, name: str, stocks: List[Stock]):
        self.name = name
        self.stocks = stocks

    def __init__(self, j):
        self.name = j["name"]
        self.stocks = [Stock]
        for st in j["stocks"]:
            self.stocks.append(Stock(st["symbol"], int(st["own"])))


def getportfolios(j):
    portfolios = [Portfolio]
    for cportfolio in j:
        print(cportfolio)
        portfolios.append(Portfolio(cportfolio))
    return portfolios
