class TradingStrategy():
    def __init__(self, name):
        self._name = name

    def generate_signal(self):
        print("This method is intended to be overridden")
        return "hold"
    
    @property
    def name(self):
        return self._name

class SMAStrategy(TradingStrategy):
    def __init__(self, swindow, lwindow):
        self._swindow = swindow
        self._lwindow = lwindow
        super().__init__("SMAStrategy")

    def generate_signal(self, price_data):
        if len(price_data[self._lwindow:]) < self._lwindow:
            return "hold"
        
        short_avg = sum(price_data[-self._swindow:]) / self._swindow
        long_avg = sum(price_data[-self._lwindow:]) / self._lwindow

        if short_avg > long_avg:
            return "buy"
        elif short_avg < long_avg:
            return "sell"
        else:
            return "hold"
        
    @property
    def swindow(self):
        return self._swindow
    
    @property
    def lwindow(self):
        return self._lwindow
        