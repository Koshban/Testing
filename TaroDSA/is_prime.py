'''
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.

is_prime(2) # -> True
is_prime(3) # -> True
is_prime(4) # -> False
is_prime(5) # -> True
is_prime(6) # -> False
is_prime(7) # -> True
is_prime(8) # -> False
is_prime(2017) # -> True
is_prime(2048) # -> False
'''

import unittest
from math import sqrt, floor
''' time = O(sqrt(n)) and Space = O(1)'''
def isprime(number: int) -> bool:
    i = 5
    if number <=1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    #for i in range(5,floor(sqrt(number)) + 1 ):
    while i ** 2 <= number:
        if number % i == 0:
            return False
        i += 6
    return True


class Testisprime(unittest.TestCase):
    def test_isprime(self):
        test_data = [
            {'input': 2, 'expected': True},
            {'input': 3, 'expected': True },
            {'input': 2017, 'expected': True },
            {'input': 2048, 'expected': False}, 
            {'input': 1, 'expected': False },
        ]
    
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = isprime(number=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}.\nGot : {actual} while expecting : {expected}")

if __name__ == "__main__":
    unittest.main()