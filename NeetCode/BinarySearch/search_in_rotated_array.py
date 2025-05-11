'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''
import unittest

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = ( l + r) // 2
            if l == r:
                pivot = l
                break            

            if nums[m] > nums[m + 1]:
                pivot = m + 1
                break
            
            if m > 0 and nums[m -1] > nums[m]:
                pivot = m
                break
            
            if nums[l] < nums[m]:
                l = m + 1
            elif nums[m] > nums[r]:
                r = m - 1
        
        l, r  = pivot, len(nums) - 1
        print(f"Pivot is at Index {pivot} with Value {nums[pivot]} for Array : {nums}")
        while l <= r:
            m = (l + r)// 2
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


class Testsearch(unittest.TestCase):
     def test_search(self):
        test_data = [            
            {'input': ([4,5,6,7,0,1,2], 0), 'expected': 4},
            {'input': ([4,5,6,7,0,1,2, 3], 3), 'expected': 7},
            {'input': ([5,6,7,1,2,4], 3), 'expected': -1},
            {'input': ([1], 8), 'expected': -1}, 
            {'input': ([8], 8), 'expected': 0}, 
            {'input': ([], 8), 'expected': -1}, 
        ]
 
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.search(nums=test_case['input'][0], target=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

