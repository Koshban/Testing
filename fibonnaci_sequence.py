"""
Fibonacci Sequence:**
   Write a function to calculate the `n`th Fibonacci number. Try to do this in a way that optimizes for time complexity.
   The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is:

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), for n > 1
To calculate the nth Fibonacci number, we can use various methods. A naive approach would be to use recursion, but this has a time complexity of O(2^n) due to the repeated calculations 
for the same values. A more time-efficient approach is to use dynamic programming with memoization or an iterative approach, both of which have a time complexity of O(n).
"""
import unittest

def fibonacci(num: int) -> int:
   if num < 0:
      return -1
   if num in (0, 1):
      return num
   a, b = 0, 1
   for n in range(2, num + 1):
      a, b = b, a + b
   return b



class TestFibonacciNumbers(unittest.TestCase):
    def test_fibonacci(self):
      test_data = [
               (0, 0),  # F(0) = 0
               (1, 1),  # F(1) = 1
               (-5, -1),  # F(-5) = -1
               (2, 1),  # F(2) = F(1) + F(0) = 1 + 0 = 1
               (3, 2),  # F(3) = F(2) + F(1) = 1 + 1 = 2
               (4, 3),  # F(4) = F(3) + F(2) = 2 + 1 = 3
               (5, 5),  # F(5) = F(4) + F(3) = 3 + 2 = 5
               (10, 55), # F(10) = 55
               (20, 6765) # F(20) = 6765
            ]
      for data, expected in test_data:
         with self.subTest(input=data, expected=expected):
            actual_result = fibonacci(num=data)
            self.assertEqual(actual_result, expected), f"Test failed for {data}. Expected : {expected}. Actual: {actual_result}"

if __name__ == "__main__":
   unittest.main()

        