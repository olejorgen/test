__author__ = 'OleJorgen'
from person import Person
class Coffe(object):
    fullname=" "
    moeny=int
    def __init__(self,fullname,money):
        self.fullname=fullname
        self.money=money
    def CoffeBuying(self,money):
        coffePrice=5
        self.money=money-coffePrice
        return money
