import numpy as np
from classes import Portfolio
from classes import FinanceAPI
tickermap = {}

def __generatetickermap(portfolios: [Portfolio], drange):
    # get all stocks async
    for cport in portfolios:
        for cs in cport.stocks:
            if cs.symbol in tickermap:
                continue
            else:
                tickermap[cs.symbol] = FinanceAPI.getdailychange(cs.symbol, drange[0], drange[1])

# drange is a tuple of 2 dates i.e. ("2016-11-01", "2016-11-30")
def calculateprofit(portfolios: [Portfolio], drange):
    __generatetickermap(portfolios, drange)
    moneyovertime = []
    for portfolio in portfolios:

        for stock in portfolio.stocks:
            __dailyprofit(tickermap[stock.symbol], stock.own)
    return moneyovertime


# stock flux is the daily change in stock prices, shares owned is the amount owned in $'s
# returns a vector of price changes in the stocks, with the last entry being
def __dailyprofit(stockflux: [float], sharesowned : float):
    zeroes = np.zeros(shape=(len(stockflux) + 1, len(stockflux)))
    for i in range(0, len(stockflux)-1):
        zeroes[i][i] = (stockflux[i]/100) + 1
        zeroes[len(zeroes)-1][i] = (stockflux[i]/100)
    # create transpose table
    return zeroes.dot(np.linalg.transpose([sharesowned]))



def printgraph(users, netprofit):
    return 0