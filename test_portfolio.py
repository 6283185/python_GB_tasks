from portfolio import *


portfolio_value = calculate_portfolio_value(stocks, prices)
most_profitable_stock = get_most_profitable_stock(stocks, prices)
portfolio_return = calculate_portfolio_return(initial_value, current_value)


print(f"Стоимость вашего портфеля: {portfolio_value}$")
print(f"Стоимость портфеля изменилась на {portfolio_return}%")
print(f"Наиболее выгодный актив в вашем портфеле: {most_profitable_stock}")
