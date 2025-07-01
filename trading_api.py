from datetime import datetime

class Trade():
    def __init__(self, strategy, signal, amount):
        self._strategy = strategy
        self._signal = signal
        self._amount = amount
        self._timestap = datetime.now()
        
    def execute(self):
        print("This method is intended to be overridden")
        return

    @property
    def strategy(self):
        return self._strategy    

    @property
    def signal(self):
        return self._signal
    
    @property
    def amount(self):
        return self._amount 
    
    @property
    def timestamp(self):
        return self._timestap

class TradingAPI:
    def __init__(self, balance):
        self._balance = balance

    def place_order(self, trade, price):
        if trade.signal == "buy" and self._balance >= trade.amount * price:
            self._balance -= trade.amount * price
            print(f"Bought {trade.amount} shares at ${price}")
        elif trade.signal == "sell":
            self._balance += trade.amount * price
            print(f"Sold {trade.amount} shares at ${price}")
        else:
            print("Invalid trade signal or Insufficient balance")

    @property
    def balance(self):
        return self._balance

