# Задача: Расчет финансовых показателей портфеля акций
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
prices_current = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

initial_value = 10000.0
current_value = 15000.0



def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    portfolio_value = 0
    for stock, quantity in stocks.items():
        portfolio_value += prices[stock] * quantity
    return portfolio_value


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return ((current_value - initial_value) / initial_value) * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    max_profit = 0
    most_profitable_stock = ""

    for stock, quantity in stocks.items():
        initial_value = prices[stock] * quantity
        current_value = prices_current[stock] * quantity  # Use prices_fresh instead of prices
        profit = ((current_value - initial_value) / initial_value) * 100

        if profit > max_profit:
            max_profit = profit
            most_profitable_stock = stock

    return most_profitable_stock

