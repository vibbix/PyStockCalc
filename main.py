import json
import sys
from classes import Portfolio, FinanceAPI
# from classes.Portfolio import Portfolio
from typing import List


def main():
    importfile = 'ex.json' if len(sys.argv) == 1 else sys.argv[1]
    portfolios = [Portfolio]
    with open(importfile) as jsonfile:
        portfolios = json.loads(jsonfile.read())
    print(portfolios)
    dc = FinanceAPI.getdailychange("amd", "2016-11-01", '2016-11-30')
    print(dc)


if __name__ == "__main__" : main()
