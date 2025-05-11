'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
import unittest
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right  = 0, len(nums) - 1
        if len(nums) == 0:
            return -1
        while left <= right:
        
            mid = left + ( right -left ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


class Testbinarysearch(unittest.TestCase):
    def test_search(self):
        test_data = [
            {'input': ([-1,0,3,5,9,12], 9), 'expected': 4},
            {'input': ([-1,0,3,5,9,12], 2), 'expected': -1},
            {'input': ([], 8), 'expected': -1}, 
        ]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.search(nums=test_case['input'][0], target=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}.\nGot : {actual} while expecting : {expected}")

if __name__ == "__main__":
    unittest.main()