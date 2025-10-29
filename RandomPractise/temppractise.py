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
import os
import logging
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FORMAT = '%(asctime)s - %(levelname)s : [%(filename)s - %(funcname)s] - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)
scriptname = os.path.splitext(os.path.abspath(__file__))[0]

logging.basicConfig(
    level = logging.DEBUG,
    format = LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f'{scriptname}.log')
    ]
)
logger = logging.getLogger()

def get_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
    args = parser.parse_args()
    return args

def string_to_int(s):
    """
    Convert string to integer without using built-in conversion
    
    Args:
        s: String to convert
        
    Returns:
        Integer value
        
    Raises:
        ValueError: For invalid inputs
        OverflowError: For numbers too large
    """
    result, is_negetive_flag, index = 0, False, 0
    if len(s) == 0:
        raise Exception("Empty String") 
    char = s[0]
    if char == "-":
        is_negetive_flag = True
        index = 1
        if len(s) == 1:
            raise ValueError("Invalid Number, just a sign")
    
    if len(s) - index > 10:
        raise OverflowError(f"Number too large: {s}")
    
    for i in range(index, len(s)):
        char = s[i]
        if not('0' <= char <= '9'):
            raise ValueError(f"Invalid character, NAN : {char}")
        digit = ord(char) - ord('0')
        result = result * 10 + digit
        if result > 2**31 -1:
            raise OverflowError(f"Number too large: {result}")
    
    return -result if is_negetive_flag else result


# Test cases
test_cases = [
    "123",      # Normal positive number
    "-456",     # Negative number
    "0",        # Zero
    "",         # Empty string
    "abc",      # Invalid characters
    "12345678901", # Overflow
    "-",        # Just minus sign
    "123a45",   # Mixed characters
    "1234567890" # Maximum valid number
]

for test in test_cases:
    try:
        result = string_to_int(test)
        print(f"'{test}' -> {result}")
    except Exception as e:
        print(f"'{test}' -> Error: {str(e)}")