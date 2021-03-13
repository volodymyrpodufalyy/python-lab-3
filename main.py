from Securities import Securities as s
from Shares import Shares
from Bonds import Bonds
from BrokerManager import BrokerManager as BM

if __name__ == '__main__':
    apple_shares = Shares("Shares of","Apple",125,"12 February", "Low", "growing", "Privilege")
    tesla_shares = Shares("Shares of","Tesla", 800, "15 February", "Medium", "descending", "Usual")
    gm_shares = Shares("Shares of","General Motors", 65, "20 February", "High", "descending", "Usual")
    clubhouse_shares = Shares("Shares of","Clubhouse", 2000, "21 February", "Extra high", "growing", "Usual")
    apple_bonds = Bonds("Bonds of","Apple", 100, "1 February", "Low", "growing", "short term", 1.25)
    google_bonds = Bonds("Bonds of","Google", 1000, "28 February", "Low", "growing", "long term", 2.35)
    microsoft_bonds = Bonds("Bonds of","Microsoft", 950, "13 February", "Medium", "growing", "medium term", 3.25)
    facebook_bonds = Bonds("Bonds of","Facebook", 220, "14 February", "High", "growing", "short term", 3.55)
    telegram_shares = Securities("Shares of ", "Telegram", 500, "24 February", "Medium", "desceding","Privilege")

    # BM.search_by_price()
    # BM.search_by_risk_level()
    # BM.search_by_trend()
    # BM.sort_by_price()
    # BM.sort_by_date()
