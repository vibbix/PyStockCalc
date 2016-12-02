import numpy as np
from classes import Portfolio
from classes import FinanceAPI
import matplotlib.pyplot as plt

__dailychange = {}
__dailyadjclose = {}

def __generatecache(portfolios: [], drange: (str, str)):
    # get all stocks async
    for portfolioiter in range(0, len(portfolios)-1):
        if portfolioiter == 0:
            continue
        cport = portfolios[portfolioiter]
        for stockiter in range(0, len(cport.stocks)-1):
            if stockiter == 0:
                continue
            cs = cport.stocks[stockiter]
            __dailyadjclose[cs.symbol] = FinanceAPI.getdailyadjclose(cs.symbol, drange[0], drange[1])
            __dailychange[cs.symbol] = FinanceAPI.getdailychange(cs.symbol, drange[0], drange[1])


# drange is a tuple of 2 dates i.e. ("2016-11-01", "2016-11-30")
def calculateprofit(portfolios: [], drange: (str, str)) -> [Portfolio.DailyProfit]:
    __generatecache(portfolios, drange)
    moneyovertime = []
    for portfolio in portfolios[1:]:
        moneyovertime.append(__calculateportfolioprofit(portfolio, drange))
    return moneyovertime


def __calculateportfolioprofit(portfolio: Portfolio.Portfolio, drange: (str, str)) -> Portfolio.DailyProfit:
    portfolioprofit = Portfolio.DailyProfit()
    portfolioprofit.name = portfolio.name
    portfolioprofit.setdaterange(drange)
    stockvalue = []
    for stock in portfolio.stocks[1:]:
        dp = Portfolio.DailyProfit()
        dp.profitdelta = FinanceAPI.getdailyrevenue(stock.symbol, stock.own, drange[0], drange[1])
        stockvalue.append(dp)
    portfolioprofit.merge(stockvalue)
    return portfolioprofit

# bug: drange does nothing, can break if cached data and drange do not match
# returns worth of stock during night
def __dailyprofitovertime(symbol: str, stocks: int, drange: (str, str)) -> Portfolio.DailyProfit:
    # np.multiply(x,y)
    adj = FinanceAPI
    v2 = np.full((1,len(adj)), stocks)


# stock flux is the daily change in stock prices, shares owned is the amount owned in $'s
# returns a vector of price changes in the stocks, with the last entry being
def __dailyprofit(stockflux: [float], sharesowned : int):
    zeroes = np.zeros(shape=(len(stockflux) + 1, len(stockflux)))
    for i in range(0, len(stockflux)-1):
        zeroes[i][i] = (stockflux[i]/100) + 1
        zeroes[len(zeroes)-1][i] = (stockflux[i]/100)
    # create transpose table
    return zeroes.dot(np.linalg.transpose([sharesowned]))


def printgraph(ldp : [Portfolio.DailyProfit]):
    # plt.xlim(ldp[0].daterange[0], ldp[0].daterange[0])
    plt.xlabel("Number of days")
    plt.ylabel("Amount in $'s")
    plt.title("Stock values over time")
    for dp in ldp:
        plt.plot(dp.profitdelta, label=dp.name)
    plt.show()
