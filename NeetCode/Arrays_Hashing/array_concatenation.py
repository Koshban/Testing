'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 '''
import unittest

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        
        for index, num in enumerate(nums):
            ans[index] = ans[index + n] = num
        return ans



class TestgetConcatenation(unittest.TestCase):
    def test_getConcatenation(self):
        test_data = [
            {'input': [1,3,2,1], 'expected': [1,3,2,1,1,3,2,1]},
            {'input': [1,2,1], 'expected': [1,2,1, 1,2,1]},            
        ]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.getConcatenation(nums = test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

        
