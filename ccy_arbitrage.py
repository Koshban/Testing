"""
**Currency Arbitrage Detection:**
    Given a table of currency exchange rates, represented as a 2D array, determine if there is an opportunity for an arbitrage; that is, whether there is some sequence of trades you 
    could make, starting with some amount of one currency, to end up with more of that currency through a series of trades.
Let's consider a simplified example with three currencies: USD (US Dollars), EUR (Euros), and GBP (British Pounds). The exchange rates are represented in a 2D array where each row and column correspond to a currency, and the value at array[i][j] represents the exchange rate from currency i to currency j.

Assuming the following exchange rates:

1 USD = 0.9 EUR
1 USD = 0.8 GBP
1 EUR = 1.1 USD
1 EUR = 0.88 GBP
1 GBP = 1.25 USD
1 GBP = 1.14 EUR
This can be represented in a 2D array as follows, where array[0][...] is USD, array[1][...] is EUR, and array[2][...] is GBP:
exchange_rates = [
    [1, 0.9, 0.8], # USD to USD, EUR, GBP
    [1.1, 1, 0.88], # EUR to USD, EUR, GBP
    [1.25, 1.14, 1] # GBP to USD, EUR, GBP
]

exchange_rates = [
    [1, 0.9, 0.8], # USD to USD, EUR, GBP
    [1.2, 1, 0.88], # EUR to USD, EUR, GBP
    [1.3, 1.14, 1] # GBP to USD, EUR, GBP
]

"""

import math

def detect_arbitrage(exchange_rates: list):
    # Convert exchange rates to negative logarithms to use Bellman-Ford
    log_exchange_rates = [[-math.log(edge) for edge in row] for row in exchange_rates]
    print(f"Exch Rates are {exchange_rates} and its Log is {log_exchange_rates}")

    # Number of currencies
    n = len(exchange_rates)
    # Initialize distances with 'infinity'
    distance = [float('inf')] * n
    # Start with any currency, here we start with the first currency (index 0)
    distance[0] = 0

    # Bellman-Ford algorithm
    for _ in range(n - 1):
        for source in range(n):
            for dest in range(n):
                if distance[dest] > distance[source] + log_exchange_rates[source][dest]:
                    distance[dest] = distance[source] + log_exchange_rates[source][dest]

    # Check for negative cycles
    for source in range(n):
        for dest in range(n):
            if distance[dest] > distance[source] + log_exchange_rates[source][dest]:
                return True  # Negative cycle found, arbitrage opportunity detected

    return False  # No negative cycle found, no arbitrage opportunity




if __name__ == "__main__":
    test_data = [
    [1, 0.9, 0.8], # USD to USD, EUR, GBP
    [1.2, 1, 0.88], # EUR to USD, EUR, GBP
    [1.3, 1.14, 1] # GBP to USD, EUR, GBP
]
    
    # Detect arbitrage
    print("Arbitrage opportunity detected:" if detect_arbitrage(exchange_rates=test_data) else "No arbitrage opportunity.")
