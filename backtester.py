# backtester.py
from strategies import SMAStrategy
import yfinance as yf
import matplotlib.pyplot as plt

symbol = "AAPL"
swindow = 5
lwindow = 15
initial_balance = 10000

# Load historical price data
data = yf.download(tickers=symbol, period="15d", interval="5m")

# Check if data is valid
if data.empty or 'Close' not in data.columns:
    raise ValueError("Failed to retrieve valid price data. Please check the ticker symbol or internet connection.")

prices = data.loc[:, ('Close', symbol)].dropna().tolist()

# Setup strategy
strategy = SMAStrategy(swindow, lwindow)

# Backtest variables
balance = initial_balance
position = 0  # number of shares
trade_history = []
portfolio_values = []

for i in range(lwindow, len(prices)):
    price_slice = prices[:i+1]
    signal = strategy.generate_signal(price_slice)
    current_price = prices[i]

    # Simulate buy/sell
    if signal == "buy" and balance >= current_price:
        position += 1
        balance -= current_price
        trade_history.append(("BUY", current_price, i))
    elif signal == "sell" and position > 0:
        position -= 1
        balance += current_price
        trade_history.append(("SELL", current_price, i))

    # Calculate current portfolio valgitue
    portfolio_value = balance + position * current_price
    portfolio_values.append(portfolio_value)

# Final report
final_price = prices[-1]
final_value = balance + position * final_price
profit = final_value - initial_balance

print(f"\nInitial Balance: ${initial_balance:.2f}")
print(f"Final Balance:   ${final_value:.2f}")
print(f"Total Profit:    ${profit:.2f}")
print(f"Total Trades:    {len(trade_history)}")

# Optional: plot portfolio growth
plt.plot(portfolio_values)
plt.title("Portfolio Value Over Time")
plt.xlabel("Time Steps")
plt.ylabel("Portfolio Value")
plt.grid()
plt.show()
