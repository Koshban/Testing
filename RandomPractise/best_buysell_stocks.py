'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''
import unittest

def buy_sell_stocks_only_once(prices: list[int]) -> int:
    if not prices or len(prices) < 2:
        return -1
    min_price = float('inf')
    max_profit = 0
    total_profit = 0
    
    for day, price in enumerate(prices):
        #print(f"For P {price} on Day: {day}.")
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
        #print(f"For P {prices[day]} on Day: {day} Max Profit is : {max_profit}, TotProfit is : {total_profit} and Sell day is {sell_day}")
    
    return max_profit

def buy_sell_multiple_times(prices: list[int]) -> int:
    if not prices or len(prices) < 2:
        return -1
    buy_price = prices[0]
    total_profit = 0
    for day, price in enumerate(prices[1:]):
        if price < buy_price:
            buy_price = price
            buy_day = day
            print(f"Buy at Price : {price} USD on Day {buy_day}")

        elif price > buy_price:
            profit = price - buy_price
            buy_price = price
            total_profit += profit
            sell_day = day
            print(f"Sell at Price : {price} USD on Day {sell_day}. Making Profit : {profit}. Total Profit so far : {total_profit}")
    
    return total_profit
        

class TestBuySellStocks(unittest.TestCase):
    def test_buy_sell_stocks(self):
        test_data_multiple = [
            ([7,1,5,3,6,4,6], 9),
           ([1,2,3,4,5], 4),
            ([7,6,4,3,1], 0),
            ([4,4,2,6,7], 5)
        ]
        for data, expected in test_data_multiple:
            with self.subTest(input=data, expected=expected):
                actual = buy_sell_multiple_times(prices=data)
                self.assertEqual(actual, expected), f"Test failed for {data}. Expected: {expected}. Actual : {actual}"
        test_data_once = [
            ([7,1,5,3,6,4,6], 5),
           ([1,2,3,4,5,5], 4),
            ([7,6,4,3,1], 0)
        ]    

        for data, expected in test_data_once:
            with self.subTest(input=data, expected=expected):
                actual = buy_sell_stocks_only_once(prices=data)
                self.assertEqual(actual, expected), f"Test failed for {data}. Expected: {expected}. Actual : {actual}"


if __name__ == "__main__":
    unittest.main()