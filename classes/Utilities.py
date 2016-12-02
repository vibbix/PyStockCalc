from datetime import datetime, timedelta
import numpy as np
__datefmt = "%Y-%m-%d"

def verifydate(datestr : str) -> datetime:
    dt = datetime.strptime(datestr, __datefmt)
    if dt > datetime.now():
        raise ValueError("date cannot be greater be in the future")
    if dt.weekday() in [5,6]: # friday, saturday
        raise ValueError("date cannot be on a weekend")
    return dt

def getformattedtoday() -> str:
    dt = datetime.now()
    return dt.__format__(__datefmt)

def getpreviousweekday(datestr: str) -> str:
    dt = datetime.strptime(datestr, __datefmt)
    dt -= timedelta(days=1)
    print(dt.weekday())
    while dt.weekday() not in [0, 1, 2, 3, 4]:  # monday through friday
        dt -= timedelta(days=1)
    return dt.__format__(__datefmt)

# adds each element of array
def ziparrays(lists_of_lists: [[]]):
    return [sum(x) for x in zip(*lists_of_lists)]

# input=5, 5; output [5,5,5,5,5]
def generatefullvector(num: int, size: int):
    return np.full((1, size), num)

def multiplyarray(x: [], y: []) -> []:
    return np.multiply(x, y)