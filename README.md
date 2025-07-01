# 🧠 Basic Trading Bot + Backtesting Framework

A simple modular trading bot with a backtesting engine written in Python. It fetches real-time data using `yfinance`, applies a strategy (e.g. SMA Crossover), and simulates trades or executes live trades through a mock API.

---

## 📌 Features

- ✅ SMA (Simple Moving Average) Crossover Strategy  
- ✅ Real-time data fetching via `yfinance`  
- ✅ Modular design using OOP principles  
- ✅ Backtesting engine with PnL calculation  
- ✅ Dummy trade execution using a mock `TradingAPI`  
- ✅ Easy to extend with custom strategies

---

## 🗂️ Project Structure

trading-bot/
│── backtester.py # Backtesting logic
│── bot.py # Live trading loop using yfinance
|── trading_api.py # api for fetching price data and executing order
├── strategies
│     ─ SMAStrategy # SMA crossover strategy class
├── main.py # Run live bot
└── README.md


---

## ⚙️ How It Works

### 🔁 Strategy

The `SMAStraregy` implements a basic moving average crossover:

```python
if short_avg > long_avg:
    return "buy"
elif short_avg < long_avg:
    return "sell"
else:
    return "hold"


🏗️ Bot Logic

Fetches price using yfinance
Generates signal using strategy
Executes trade via TradingAPI (mock)

📈 Backtesting

Simulates trades based on historical data
Evaluates performance (PnL, trades, win/loss)

🚀 Getting Started

1. Clone the repository
git clone https://github.com/yourusername/trading-bot.git
cd trading-bot

2. Install dependencies
pip install -r requirements.txt

3. Run backtest
python run_backtest.py

4. Run live bot (uses yfinance live price)
python run_live.py

🧪 Example Output

Current price: 183.12
Generated signal: buy
Bought 1 shares at $183.12
Remaining balance: 9816.88

📚 Requirements

Python 3.8+
yfinance
pandas
matplotlib (optional for plotting)