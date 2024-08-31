'''A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
You must write an algorithm that runs in O(n) time.

Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Input: nums = [2,20,4,10,3,4,5]
Output: 4

'''
import unittest

def longest_sequence(elements: list[int]) -> int:
    numSet = set(elements)
    longest_seq = 0
    for n in elements: 
        if (n-1) not in numSet:# find if its start of a sequence
            length = 0
            while ( n + length) in numSet: # keep on finding the next consecutive number 
                length += 1
                
            longest_seq = max(longest_seq, length)        
    return longest_seq

class Test_longest_sequence(unittest.TestCase):
    def test_longest_sequence(self):
        test_data =[
            {'input': [0,3,2,5,4,6,1,1], 'expected': 7},
            {'input': [2,20,4,10,3,4,5], 'expected': 4},
            {'input': [100,4,200,1,3,2], 'expected': 4},
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = longest_sequence(elements=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case['input']}. Expected {expected} but got {actual}")

if __name__ == "__main__":
    unittest.main()
