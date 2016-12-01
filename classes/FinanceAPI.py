import yahoo_finance as yf


def getdailychange(symbol, startdate, enddate) -> [float]:
    sym = yf.Share(symbol)
    history = sym.get_historical(startdate, enddate)
    history.reverse()
    change = [float]
    dayclose = float(history[0]["Adj_Close"])
    for day in history[1:]:
        cdayclose = float(day["Adj_Close"])
        diff = cdayclose-dayclose
        percent = diff/dayclose
        dayclose = cdayclose
        change.append(percent*100)
    return change[1:]