"""
**Stock Buy and Sell:**
You are given an array for which the `i`th element is the price of a given stock on day `i`. If you were only permitted to complete at most one transaction (i.e., buy one and sell one 
share of the stock), design an algorithm to find the maximum profit.

We'll create an array of stock prices representing the price of a stock on consecutive days. The goal is to find the best day to buy and the best day to sell to maximize the profit,
with the constraint that you must buy before you sell.

Here's an example of how the stock prices could look like over a period of days, and the possible maximum profit:

Day 0: Price = $100
Day 1: Price = $180
Day 2: Price = $260
Day 3: Price = $40
Day 4: Price = $300
Day 5: Price = $90
In this case, the best day to buy would be Day 0 when the price is $100, and the best day to sell would be Day 4 when the price is $300, resulting in a maximum profit of $200.

The test data could comprise various scenarios, including increasing prices, decreasing prices, mixed fluctuations, and no possible profit scenarios. Let's create an array of test
cases with the expected maximum profit:

"""

def find_max_profit_ON2(input_data: list):
    if not input_data:
        return 0
    
    price_diff = 0
    temp_data = list(reversed(input_data))
    for day,price in enumerate(temp_data):
        print(f'Day {day}, price {price}')
        for next_price in temp_data[day + 1 : ]:
            price_diff = max(price_diff, price - next_price)
            print(f'price DIff {price_diff}, Next price {next_price}')

    print(price_diff)
    return price_diff

def find_max_profit_ON(input_data: list):
    if not input_data or len(input_data) < 2:
        return 0, None, None
    min_price = float('inf')
    max_profit = 0
    for price in input_data:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == "__main__":
    test_data = [
    ([100, 180, 260, 40, 300, 90], 260), # Example 1: Buy on Day 3, Sell on Day 4
    ([7, 1, 5, 3, 6, 4], 5),             # Example 2: Buy on Day 1, Sell on Day 4
    ([7, 6, 4, 3, 1], 0),                # Example 3: No profit is possible
    ([1, 2, 3, 4, 5], 4),                # Example 4: Buy on Day 0, Sell on Day 4
    ([3, 3, 3, 3, 3], 0),                # Example 5: No profit is possible, price is constant
    ([8, 10, 2, 5, 11, 1], 9),           # Example 6: Buy on Day 2, Sell on Day 4
    ]
    for data, result in test_data:
        assert find_max_profit_ON2(input_data=data) == result, f"Failed for {data} on find_max_profit_ON2"
        assert find_max_profit_ON(input_data=data) == result, f"Failed for {data} on find_max_profit_ON"
        
