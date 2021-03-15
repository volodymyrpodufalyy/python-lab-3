from Securities import RiskLevel as r
from Securities import TradingTrend as t
from SecuritiesTypes.Shares import Shares
from SecuritiesTypes.Bonds import Bonds
from BrokerManager import BrokerManager as BM

if __name__ == '__main__':
    apple_shares = BM().add_securities([Shares("Shares of", "Apple", 125, "11 February", r.LOW.name, t.GROWING.name, "Privilege")])
    tesla_shares = BM().add_securities([Shares("Shares of","Tesla", 800, "15 February", r.MEDIUM.name, t.DESCENDING.name, "Usual")])
    gm_shares = BM().add_securities([Shares("Shares of","General Motors", 65, "20 February", r.HIGH.name, t.DESCENDING.name, "Usual")])
    clubhouse_shares = BM().add_securities([Shares("Shares of","Clubhouse", 2000, "21 February", r.EXTRAHIGH.name, t.GROWING.name, "Usual")])
    apple_bonds = BM().add_securities([Bonds("Bonds of","Apple", 100, "1 February", r.LOW.name,t.GROWING.name, "short term", 1.25)])
    google_bonds = BM().add_securities([Bonds("Bonds of","Google", 1000, "28 February", r.LOW.name, t.GROWING.name, "long term", 2.35)])
    microsoft_bonds = BM().add_securities([Bonds("Bonds of","Microsoft", 950, "13 February",  r.MEDIUM.name, t.GROWING.name, "medium term", 3.25)])
    facebook_bonds = BM().add_securities([Bonds("Bonds of","Facebook", 220, "14 February", r.HIGH.name, t.GROWING.name, "short term", 3.55)])
    telegram_shares = BM().add_securities([Shares("Shares of ", "Telegram", 500, "24 February", r.MEDIUM.name, t.DESCENDING.name,"Privilege")])
    BM().print_securities()
    # BM().search_by_price()
    # BM().search_by_risk_level("MEDIUM")
    # BM().search_by_trend("GROWING")
    # BM().sort_by_price()
    # BM().sort_by_date()
