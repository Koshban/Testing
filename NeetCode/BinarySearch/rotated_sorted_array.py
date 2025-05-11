'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. 
For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4
'''
import unittest
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) <= 1:
            return -1
        while l <= r:
            m = (l + r) // 2
            if l == r:  # If we have reached a point where left=right, we found the pivot
                indexatrotate = l
                return nums[indexatrotate]
            
            if nums[m] > nums[m + 1]: # Compare mid with mid+1. If mid is greater, mid+1 is pivot
                indexatrotate = m + 1
                return nums[indexatrotate]
            
            if m > 0 and nums[m -1] > nums[m]:
                indexatrotate = m
                return nums[indexatrotate]
            if nums[l] <= nums[m]:
                l = l + 1
            elif nums[m] > nums[r]:
                r = r -1



class TestfindMin(unittest.TestCase):
    def test_findMin(self):
        test_data = [
            {'input': [3,4,5,6,1,2], 'expected': 1},
            {'input': [3,4,5,1,2], 'expected': 1},
            {'input': [4,5,0,1,2,3], 'expected': 0},
            {'input': [4,5,6,7,3], 'expected': 3},
            {'input': [], 'expected': -1}, 
            {'input': [9], 'expected': -1}, 
        ]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.findMin(nums=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()