from Securities import Securities

class BrokerManager:
    # return obj
    def search_by_price():
        price_of = int(input("Enter the price of interested security "))
        for item in Securities.securities_list:
            if item.price == price_of:
                print(item.type + " " +  item.brand + "\tPrice:" +str(item.price) + "\tDate of buying:" + item.buying_date
                      + "\tStatus:" + item.trading_trend)

    def search_by_risk_level():
        risk_of = input("Enter the risk level of interested security ")
        for item in Securities.securities_list:
            if item.risk_level == risk_of:
                print(item.type + " " + item.brand + "\tPrice:" +str(item.price) +"\tRisk level:" +item.risk_level +
                      "\tDate of buying:" + item.buying_date + "\tStatus:" + item.trading_trend)

    def search_by_trend():
        trend_of = input("Enter the trading trend of interested security ")
        for item in Securities.securities_list:
            if item.trading_trend == trend_of:
                print(item.type + "  " + item.brand + "\tPrice:" +str(item.price) + "\tDate of buying:" +
                      item.buying_date + "\tStatus:" + item.trading_trend)

    def sort_by_price():
        sorted_securities_price = []
        trend_of = input("Enter the trading trend of interested security ")
        for item in Securities.securities_list:
            if item.trading_trend == trend_of:
                print(item.type + "  " + item.brand + "\tPrice:" + str(item.price) + "\tDate of buying:" +
                      item.buying_date + "\tStatus:" + item.trading_trend)
                sorted_securities_price.append(item)
        print("\n\nSecurities sorted by price from smallest to biggest:\n")
        sorted_securities = sorted(sorted_securities_price, key=lambda e: e.price)
        print(*sorted_securities)
        print("\n\nSecurities sorted by price from biggest to smallest:\n")
        sorted_securities = sorted(sorted_securities_price, key=lambda e: e.price, reverse=True)
        print(*sorted_securities)

    def sort_by_date():
        sorted_securities_trend = []
        risk_of = input("Enter the risk level of interested security ")
        for item in Securities.securities_list:
            if item.risk_level == risk_of:
                print(item.type + " " + item.brand + "\tPrice:" +str(item.price) +"\tRisk level:" +item.risk_level +
                      "\tDate of buying:" + item.buying_date + "\tStatus:" + item.trading_trend)
                sorted_securities_trend.append(item)
        print("\n\nFrom oldest to newest:\n")
        sorted_securities = sorted(sorted_securities_trend, key=lambda e: e.buying_date)
        print(*sorted_securities)
        print("\n\nFrom newest to oldest:\n")
        sorted_securities = sorted(sorted_securities_trend, key=lambda e: e.buying_date, reverse=True)
        print(*sorted_securities)