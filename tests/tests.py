from unittest import TestCase
from classes import Utilities, Portfolio, StockCalc

class TestUtilities(TestCase):
    def multiarray(self):
        v1 = [5,5,5,5]
        v2 = [1,2,3,4]
        self.assertEqual([5,10,15,20], Utilities.multiplyarray(v1,v2))
    def testpreviousweekday(self):
        day = "2016-11-12"
        pv = Utilities.getpreviousweekday(day)
        self.assertEqual("2016-11-10", pv)

