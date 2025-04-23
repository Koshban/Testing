'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
import unittest

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        
        for l in range(0, len(nums)):
            print(f" Outside. Nums is {nums} and L is {l} and K is {k}")
            if nums[l] != val:
                print(f" 1. Nums is {nums} and L is {l} and K is {k}")
                nums[k] = nums[l]
                k += 1    
                print(f" 2. Nums is {nums} and L is {l} and K is {k}")           
             
        return (k, nums[:k])

class TestremoveElement(unittest.TestCase):
    def test_removeElement(self):
        test_data = [
            {'input': ([0,1,2,2,3,0,4,2], 2), 'expected': (5, [0,1,3,0,4])},
            {'input': ([3,2,2,3], 3), 'expected': (2, [2,2])},            
        ]
        soln = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = soln.removeElement(nums=test_case['input'][0], val=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

