import json
import sys
from classes import Portfolio, FinanceAPI
# from classes.Portfolio import Portfolio
from typing import List


def main():
    importfile = 'ex.json' if len(sys.argv) == 1 else sys.argv[1]
    portfolios = [Portfolio]
    with open(importfile) as jsonfile:
        p = json.loads(jsonfile.read())
        portfolios = Portfolio.getportfolios(p)
    results = {} # [{"name": str, "profitdelta": [float]}]
    for portfolio in portfolios[1:]:
        cresult = {}
        cresult["name"] = portfolio.name
        cresult["profitdelta"] =  [float]


if __name__ == "__main__" : main()
