'''
**Fibonacci Sequence:**
Write a function to calculate the `n`th Fibonacci number. Try to do this in a way that optimizes for time complexity.
F(n) = F(n-1) + F(n-2)
Base cases:
F(0) = 0
F(1) = 1
F(3) = F(2) + F(1)
  2  =  1   +   1

F(4) = F(3) + F(2)
  3  =  2   +   1

F(5) = F(4) + F(3)
  5  =  3   +   2
'''
import unittest
import logging
import os

script_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig(
    level = logging.DEBUG,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f'{script_name}.log')
    ]
)

logging.info(f"Script is {script_name}")


def fibonacci_recursive(num: int) ->int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci_recursive(num - 2 ) + fibonacci_recursive(num - 1 ) 

def fibonacci_iterative(num: int) ->int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, num + 1 ):
        a, b = b, a + b
    return b

from datetime import datetime, timedelta
from functools import lru_cache, wraps
import time


def expiring_lru_cache(seconds, maxsize=128):
    def decorator(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped

    return decorator


@expiring_lru_cache(seconds=4)
def fib_numbers(num: int) -> int:
    print(f'  : Miss {num}')
    if 0 >= num >= 1:
        return 1
    if num < 0:
        return -1

    return fib_numbers(num - 1) + fib_numbers(num - 2)


for num, i in enumerate(range(6)):
    print(f'fib_numbers({num})')
    result = fib_numbers(num)
    print(f'  : Result={result}')
    time.sleep(1)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        test_cases = [
            {
                'input': 0,
                'expected': 0,
                'description': 'F(0) = 0'
            },
            {
                'input': 1,
                'expected': 1,
                'description': 'F(1) = 1'
            },
            {
                'input': 2,
                'expected': 1,
                'description': 'F(2) = F(1) + F(0) = 1'
            },
            {
                'input': 3,
                'expected': 2,
                'description': 'F(3) = F(2) + F(1) = 2'
            },
            {
                'input': 7,
                'expected': 13,
                'description': 'F(7) = F(6) + F(5) = 13'
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                n = test_case['input']
                expected = test_case['expected']
                
                # Test both implementations
                recursive_result = fibonacci_recursive(n)
                #iterative_result = fibonacci_iterative(n)
                
                logging.info(f"\nTesting n={n}")
                logging.info(f"Sequence up to F({n}):")
                self.print_sequence(n)
                logging.info(f"Expected: {expected}")
                logging.info(f"Recursive result: {recursive_result}")
                #logging.info(f"Iterative result: {iterative_result}")
                
                self.assertEqual(recursive_result, expected)
                #self.assertEqual(iterative_result, expected)

    def print_sequence(self, n):
        """Helper method to print Fibonacci sequence up to n"""
        sequence = []
        a, b = 0, 1
        for i in range(n + 1):
            sequence.append(a)
            a, b = b, a + b
        logging.info(f"{sequence} (showing F(0) to F({n}))")

if __name__ == '__main__':
    unittest.main(verbosity=2)




