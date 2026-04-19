from src.data_loader import get_data
from src.optimizer import optimize_portfolio
from src.utils import plot_efficient_frontier

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

    data = get_data(tickers)

    weights, returns, risk = optimize_portfolio(data)

    print("\nOptimal Weights:")
    for t, w in zip(tickers, weights):
        print(f"{t}: {w:.4f}")

    print(f"\nExpected Return: {returns:.4f}")
    print(f"Risk (Volatility): {risk:.4f}")

    plot_efficient_frontier(data)

if __name__ == "__main__":
    main()