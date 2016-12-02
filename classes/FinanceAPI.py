import yahoo_finance as yf
from classes import Utilities
import operator
__dailyadjcache = {}
__st = ""
__dt = ""

# Gets the closing time
# bug -> does not check start/end date correctly
def getdailyadjclose(symbol: str, startdate: str, enddate: str) -> [float]:
    Utilities.verifydate(startdate)
    Utilities.verifydate(enddate)
    # bug: does not verify the date range matches. would require a more extensive cache system
    if symbol in __dailyadjcache.keys():
        return __dailyadjcache[symbol]
    share = yf.Share(symbol)
    history = share.get_historical(startdate, enddate)
    history.reverse()
    adjclose = [float]
    for h in history:
        adjclose.append(float(h["Adj_Close"]))
    __dailyadjcache[symbol] = adjclose
    return adjclose


# gets the daily change in percentage between nights
def getdailychange(symbol: str, startdate: str, enddate: str) -> [float]:
    history = getdailyadjclose(symbol, startdate, enddate)
    change = [float]
    dayclose = history[1]
    for day in history[2:]:
        cdayclose = day
        diff = cdayclose - dayclose
        percent = diff/dayclose
        dayclose = cdayclose
        change.append(percent*100)
    return change[1:]

def getdailyrevenue(symbol: str, stocks: int, startdate: str, enddate: str) -> [float]:
    adj = getdailyadjclose(symbol, startdate, enddate)[1:]
    v2 = Utilities.generatefullvector(stocks, len(adj))[0]
    return Utilities.multiplyarray(adj[1:], v2[0])
