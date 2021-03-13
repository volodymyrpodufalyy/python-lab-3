class Securities:
    securities_list = []
    def __init__(self,type,brand,price,buying_date,risk_level,trading_trend):
            self.price = price
            self.brand = brand
            self.risk_level = risk_level
            self.trading_trend = trading_trend
            self.buying_date = buying_date
            self.type = type
            self.securities_list.append(self)

    def __del__(self):
        del self

    def __str__(self):
        return f"{self.type} {self.brand}\nPrice:{self.price}\nDate of Buying:{self.buying_date}\n" \
               f"Risk level:{self.risk_level}\nTrading trend:{self.trading_trend}\n"

