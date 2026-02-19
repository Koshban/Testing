'''
Find a duplicate, Space Edition™.
We have a list of integers, where:
The integers are in the range 1..n
The list has a length of n+1
It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.
Write a function which finds an integer that appears more than once in our list. Don't modify the input! (If there are multiple duplicates, you only need to find one of them.)
So we need to optimize for space!
'''

import os
import unittest
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scriptname = os.path.splitext(os.path.abspath(__file__))[0]
LOG_FORMAT = '%(asctime)s - %(levelname)s -[%(filename)s - %(funcName)s] : %(message)s'
logsdir = os.path.join(BASE_DIR,"logs")
os.makedirs(logsdir, exist_ok=True)
logpath = os.path.join(logsdir, f'{scriptname}.log')
logging.basicConfig(
    level = logging.DEBUG,
    format = LOG_FORMAT,
    handlers= [
        logging.StreamHandler(),
        logging.FileHandler(logpath)
    ]
)
logger = logging.getLogger(__name__)
def find_duplicate(nums: list[int]) -> int:
    stangingdict = {}
    for num in nums:
        try:
            if isinstance(num, int):
                if num not in stangingdict.keys():
                    stangingdict[num] = 1
                else:
                    return num
            else:
                logger.error((f"Error encountered: Num {num} is not an integer."))
            
        except Exception as e:
            logger.error((f"Error encountered: {e}"))
            return
class TestFIndDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        test_data = [
            {'input': [1, 2, 2, 3], 'expected': [2], 'desc': "Basic duplicate with value 2"},
            {'input': [1, 3, 4, 2, 2], 'expected': [2], 'desc': "Duplicate at end with value 2"},
            {'input': [2, 2, 2, 2, 2], 'expected': [2], 'desc': "All same numbers"},
            {'input': [1, 1, 2, 3, 4], 'expected': [1], 'desc': "Duplicate at start with value 1"},
            {'input': [1, 2, 3, 3, 4, 5], 'expected': [3], 'desc': "Middle duplicate with value 3"},
            {'input': [5, 4, 3, 2, 1, 2], 'expected': [2], 'desc': "Reverse sorted with duplicate 2"},
            {'input': [1, 2, 3, 4, 4, 5, 6], 'expected': [4], 'desc': "Sorted with duplicate 4"},
            {'input': [1, 1, 2, 2, 3, 3], 'expected': [1, 2, 3], 'desc': "Multiple pairs of duplicates"},
            {'input': [3, 1, 2, 3, 4, 3], 'expected': [3], 'desc': "Triple occurrence of 3"},
            {'input': [7, 5, 3, 'N', 4, 6, 'M', 1], 'expected': [7], 'desc': "Random order with duplicate 7"}
        ]
        for test_case in test_data:
            actual = find_duplicate(test_case['input'])
            expected = test_case['expected']
            logger.info(f"Testing case: {test_case['desc']}")
            logger.info(f"Input: {test_case['input']}")
            self.assertTrue(actual in expected, 
                   f"Failed for {test_case['input']} as output from the Function was {actual} but expected was {expected}")
            logger.info(f"Test passed! Found duplicate: {actual}\n")


if __name__ == "__main__":
    unittest.main()




