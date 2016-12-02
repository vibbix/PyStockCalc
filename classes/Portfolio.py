from datetime import datetime
from classes import Utilities

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
        self.stocks = [Stock]

    def __init__(self, name: str, stocks: [Stock]):
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


class DailyProfit(object):
    def __init__(self):
        self.name = str
        self.profitdelta = [float]
        self.daterange = (datetime, datetime)


    def setdaterange(self, dr : (str, str)):
        dr1 = Utilities.verifydate(dr[0])
        dr2 = Utilities.verifydate(dr[0])
        self.daterange = (dr1, dr2)

    # dp is a list daily profits
    def merge(self, dp: []):
        dps = [self.profitdelta]
        for cdp in dp:
            dps.append(cdp.profitdelta)
        self.profitdelta = Utilities.ziparrays(dps[1:])
