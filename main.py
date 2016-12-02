import json
import sys
from classes import Portfolio, StockCalc, Utilities
# from classes.Portfolio import Portfolio
from typing import List


def main():
    importfile = 'ex.json' if len(sys.argv) == 1 else sys.argv[1]
    portfolios = []
    with open(importfile) as jsonfile:
        p = json.loads(jsonfile.read())
        portfolios = Portfolio.getportfolios(p)
    profit = StockCalc.calculateprofit(portfolios, ("2016-01-01", Utilities.getformattedtoday()))
    StockCalc.printgraph(profit)

if __name__ == "__main__" : main()
