'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]

Input: nums = [4,5,6], target = 10
Output: [0,2]

'''
import unittest

def pair_sum(pairs: list[int], target: int) -> list[int]:
    nums_hashmap = {}
    for idx, num in enumerate(pairs):
        difference = target - num
        if difference in nums_hashmap.keys():
            return [nums_hashmap[difference], idx]
        nums_hashmap[num] = idx
    return [-1]

class TestPairSums(unittest.TestCase):
    def test_pair_sum(self):
        test_data = [
            {'input': [[3, 4, 5, 6], 7], 'expected': [0,1]},
            {'input': [[4, 5, 6], 10], 'expected': [0,2]},
            {'input': [[2, 7, 11, 15], 9], 'expected': [0,1]},
            {'input': [[2, 1, 5, 3], 4], 'expected': [1,3]},
            {'input': [[2, 1, 5, 3], 10], 'expected': [-1]},
            {'input': [[3, 2, 5, 4, 1], 8], 'expected': [0, 2]},
            {'input': [[4, 7, 9, 2, 5, 1], 5], 'expected': [0, 5]},
            {'input': [[4, 7, 9, 2, 5, 1], 3], 'expected': [3, 5]},
        ]

        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = pair_sum(pairs=test_case['input'][0], target=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Expected {expected} but got in actual {actual}")

if __name__ == "__main__":
    unittest.main()
