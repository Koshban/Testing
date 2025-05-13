'''
**Missing Number in Sequence:**
Given a list of `n-1` integers in the range from 1 to `n`, there’s no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the 
missing integer.
'''

import unittest
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)


def find_missing_number(integerslist: list[int]) -> int:
    if not integerslist or not isinstance(integerslist, list) or len(set(integerslist)) != len(integerslist):
        return -1
    n = len(integerslist) + 1
    total_sum = int(n * (n + 1)//2)
    return total_sum - sum(integerslist)
     

class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        test_data = [            
            {
                'input': [1, 2, 4, 5],
                'expected': 3,  # Missing number in middle
            },
            {
                'input': [2, 3, 4, 5],
                'expected': 1,  # Missing first number
            },
            {
                'input': [1, 2, 3, 4],
                'expected': 5,  # Missing last number
            },
            {
                'input': [],
                'expected': -1,  # Empty list
            },
            {
                'input': [2],
                'expected': 1,  # Missing first number in list of length 1
            },
            {
                'input': [1],
                'expected': 2,  # Missing second number in list of length 1
            },
            {
                'input': [1, 3, 4, 5, 6, 7, 8, 9, 10],
                'expected': 2,  # Missing early number in long sequence
            },
            {
                'input': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'expected': 10,  # Missing last number in long sequence
            },
            {
                'input': [2, 3, 4, 5, 6, 7, 8, 9, 10],
                'expected': 1,  # Missing first number in long sequence
            },
            {
                'input': [1, 2, 3, 5],
                'expected': 4,  # Basic case
            }
        ]
 
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = find_missing_number(test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

    def test_invalid_inputs(self):
        # Additional test cases for invalid inputs
        test_data = [
            {
                'input': [-1, 2, 3],  # Negative numbers
                'expected': -1
            },
            {
                'input': [1, 1, 2, 3],  # Duplicates
                'expected': -1
            },
            {
                'input': [0, 1, 2],  # Zero included
                'expected': 3
            }
        ]

        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = find_missing_number(test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

    def test_large_numbers(self):
        # Test with larger sequences
        large_sequence = list(range(1, 1001))  # 1 to 1000
        large_sequence.remove(500)  # Remove 500
        self.assertEqual(find_missing_number(large_sequence), 500)

if __name__ == '__main__':
    unittest.main()