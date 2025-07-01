import time
from strategies import SMAStrategy
from trading_api import TradingAPI
from bot import Bot

if __name__ == "__main__":
    symbol = 'AAPL'

    api = TradingAPI(balance=10000)
    strategy = SMAStrategy(swindow=3, lwindow=5)
    system = Bot(api, strategy, symbol)

    for _ in range(10):
        system.run()
        print(f"Remaining balance: {api.balance}")
        time.sleep(60)

    print(f"Final balance: {api.balance}")  