'''
3. **Merge Overlapping Intervals:**
   Given a collection of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals as they appear.
'''
import unittest
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s- %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def merge_intervals(testlist: list[list[int]]) -> list[int]:
    inbetweener, starter = 0, 0
    resultant = []
    if len(testlist) < 1:
        return resultant
    
    
    # Sort intervals based on start element. Example: [[2,6], [1,3], [8,10]] becomes [[1,3], [2,6], [8,10]]
    testlist.sort(key=lambda x:x[0])

    result = [testlist[0]] # Step 3: Initialize result with first interval
    logging.info(f"1. Result is : {result}")

    # Step 4: Iterate through remaining intervals
    if len(testlist) > 1:
        for current in testlist[1:]:
            previous = result[-1] 
            logging.info(f"2. Current is: {current} and previous is: {previous} and result is: {result}")
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
                logging.info(f"3. Current is: {current} and previous is: {previous} and result is: {result}")
            else:
                result.append(current)
                logging.info(f"4. Current is: {current} and previous is: {previous} and result is: {result}")
        logging.info(f"5. Current is: {current} and previous is: {previous} and result is: {result}")
    

    return result

class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        test_data = [            
            {
                'input': [[1,3], [2,6]],
                'expected': [[1,6]],  # Simple overlap
            },
            {
                'input': [[1,2], [3,4], [5,6]],
                'expected': [[1,2], [3,4], [5,6]],  # No overlapping intervals
            },
            {
                'input': [[1,4], [4,5], [2,3]],
                'expected': [[1,5]],  # Multiple overlapping intervals
            },
            {
                'input': [],
                'expected': [],  # Empty input
            },
            {
                'input': [[1,3]],
                'expected': [[1,3]],  # Single interval
            },
            {
                'input': [[1,3], [2,6], [8,10], [15,18]],
                'expected': [[1,6], [8,10], [15,18]],  # Complex case
            },
            {
                'input': [[1,5], [2,3], [3,4]],
                'expected': [[1,5]],  # Completely overlapping intervals
            },
            {
                'input': [[1,2], [2,3], [3,4]],
                'expected': [[1,4]],  # Touching intervals
            },
            {
                'input': [[2,6], [1,3], [8,10], [15,18]],
                'expected': [[1,6], [8,10], [15,18]],  # Unsorted intervals
            },
            {
                'input': [[1,10], [2,3], [4,5], [6,7]],
                'expected': [[1,10]],  # One interval encompasses all others
            }
        ]
 
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = merge_intervals(test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()