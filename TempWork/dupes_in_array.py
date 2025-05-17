'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of an array), some elements appear twice and others appear once. Find all the elements that appear twice in this array. 
Could you do it without extra space and in O(n) runtime?
'''
import unittest
import os
import logging

script_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{script_name}.log'),
        logging.StreamHandler()
    ]
)

def findDuplicates(dupeslist: list[int]) -> list[int]:
    result = set()
    logging.info(f"Starting with {dupeslist}")
    for num in dupeslist:
        # Get the absolute value since we might have marked it negative
        index = abs(num) - 1 # For 0 based Index
        # If the number at index is positive, make it negative
        # If it's already negative, we've seen this number before
        if dupeslist[index] > 0: # First time seeing this number ie if the num is > 0 then its the 1st time we seeing this
            logging.info(f"1 : Val for Index {index} is {dupeslist[index]}")
            dupeslist[index] = -dupeslist[index] # Mark it negetive so easier to keep track
            logging.info(f"2 : After negeting Val for Index {index} is {dupeslist[index]}")
        else: # Already negative = we've seen this before
            result.add(abs(num)) # It's a duplicate
            logging.info(f"3 : Result is now {result}")
    
    return result

class TestFindDuplicates(unittest.TestCase):
    def test_find_duplicates(self):
        test_data = [
            {'input': [4,3,2,7,8,2,3,1], 'expected': [2,3]},
            {'input': [1,1,2], 'expected': [1]},
            {'input': [1], 'expected': []},
            {'input': [1,2,3,4,5], 'expected': []},
            {'input': [1,1,1,1,1], 'expected': [1]},
            {'input': [1,2,2,3,3,4,4,5,5], 'expected': [2,3,4,5]},
            {'input': [5,5,5,4,4,4,3,3,3], 'expected': [3,4,5]},
            {'input': [1,2,3,3,2,1], 'expected': [1,2,3]},
            {'input': [10,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,10], 'expected': [1,2,3,4,5,6,7,8,9,10]},
            {'input': [2,2], 'expected': [2]},
            {'input': [3,3,3], 'expected': [3]},
            {'input': [1,2,3,4,3,2,1], 'expected': [1,2,3]},
            {'input': [5,4,3,2,1,1,2,3,4,5], 'expected': [1,2,3,4,5]},
            {'input': [1,2,2,3,3,3], 'expected': [2,3]},
            {'input': [4,4,4,4], 'expected': [4]}
        ]
        
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = findDuplicates(test_case["input"].copy())  # Using copy to preserve original input
                expected = test_case["expected"]
                # Sort both lists for comparison since order doesn't matter
                self.assertEqual(sorted(actual), sorted(expected), 
                               f"Failed for {test_case}. Actual {actual} but expected {expected}")

if __name__ == "__main__":
    unittest.main()