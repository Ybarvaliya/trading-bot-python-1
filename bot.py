import yfinance as yf
from trading_api import Trade

# Bot 
# 1. Fetches price data (class TradingAPI using yfinance)
# 2. Generates signal (class SMAStrategy with the fetched price data)
# 3. Creates trade (class Trade uses details like signal, amount and strategy)
# 4. Executes trade (class TradingAPI)

class Bot():
    def __init__(self, api, strategy, symbol):
        self._api = api
        self._strategy = strategy
        self._symbol = symbol
        self._price_data = []

    def fetch_price_data(self):
        
        data = yf.download(tickers = self._symbol, period="1d", interval="1m")

        if not data.empty:
            price = data['Close'].iloc[-1]
            self._price_data.append(price)
            if(len(self._price_data) > self._strategy.lwindow):
                self._price_data.pop(0)
            print(f"Current price: {price}")
        else:
            print("Failed to fetch price data")

    def run(self):
        self.fetch_price_data()
        signal = self._strategy.generate_signal(self._price_data)
        print(f"Generated signal: {signal}")

        if signal in ["buy", "sell"]:
            trade_instance = Trade(self.fetch_strategy(), signal, 1)
            self._api.place_order(trade_instance, self._price_data[-1])

    @property
    def api(self):
        return self._api
    
    @property
    def strategy(self):
        return self._strategy
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def price_data(self):
        return self._price_data
    


