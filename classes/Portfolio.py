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
        self.stocks = List[Stock]
        for st in j["stocks"]:
            self.stocks += Stock(st["symbol"], st["own"])


def GetPortfolios(j):
    portfolios = [Portfolio]
    for portfolio in j:
        portfolios += Portfolio(portfolio)
    return portfolios
