from Securities import Securities
from Securities import RiskLevel
from Securities import TradingTrend

class BrokerManager:
    securities = []

    def add_security(self, security: Securities):
        self.securities.append(Securities)

    def add_securities(self, securities: list):
        self.securities += securities

    def search_by_price(self):
        price_of = int(input("Enter the price of interested security "))
        for item in self.securities:
            if item.price == price_of:
                print(item)

    def search_by_risk_level(self, risk_level = RiskLevel):
        for item in self.securities:
            if item.risk_level == risk_level:
                print(item)

    def search_by_trend(self,trading_trend = TradingTrend):
        # trading_trend = input("Enter the trading trend of interested security ")
        for item in self.securities:
            if item.trading_trend == trading_trend:
                print(item)

    def print_securities(self):
        for item in self.securities:
            print(item)

    def sort_by_price(self):
        sorted_securities_price = []
        # trend_of = input("Enter the trading trend of interested security ")
        for item in self.securities:
                sorted_securities_price.append(item)
        print("\n\nSecurities sorted by price from smallest to biggest:\n")
        sorted_securities = sorted(sorted_securities_price, key=lambda e: e.price)
        print(*sorted_securities)
        print("\n\nSecurities sorted by price from biggest to smallest:\n")
        sorted_securities = sorted(sorted_securities_price, key=lambda e: e.price, reverse=True)
        print(*sorted_securities)

    def sort_by_date(self):
        sorted_securities_buying_date = []
        for item in self.securities:
                sorted_securities_buying_date.append(item)
        print("\n\nFrom oldest to newest:\n")
        sorted_securities = sorted(sorted_securities_buying_date, key=lambda e: e.buying_date)
        print(*sorted_securities)
        print("\n\nFrom newest to oldest:\n")
        sorted_securities = sorted(sorted_securities_buying_date, key=lambda e: e.buying_date, reverse=True)
        print(*sorted_securities)


