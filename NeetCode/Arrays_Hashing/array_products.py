'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n) time without using the division operation?

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''
import unittest
import math

def productExceptSelf_usingdivison(nums: list[int]) -> list[int]:
    staging_list = []
    product = 1
    if len(nums) < 1:
        return [-1]
    for number in nums:
        if number != 0:
            product *= number
        else:
            product = product
    print(f"Product of {nums} is {product}")
    for idx, number in enumerate(nums): 
        if 0 in nums and number != 0:
            staging_list.append(0)
        elif 0 not in nums:
            staging_list.append(product//number)
        else:
            staging_list.append(product)
    return staging_list

def productExceptSelf(nums: list[int]) -> list[int]:
    staging_list = []
    product_pre, product_post = 1, 1
    if len(nums) < 1:
        return [-1]
    prefix, postfix = [], []
    length = len(nums)
    for idx, number in enumerate(nums):
        print(f"At Idx {idx}. So length -idx is {length -idx -1}")
        product_pre *= number
        product_post *= nums[length -idx -1]
        prefix.append(product_pre)
        postfix.insert(0, product_post)
        print(prefix)
        print(postfix)
    for idx, number in enumerate(nums):
        if idx == 0:
            prefixnum = 1
            postfixnum = postfix[idx + 1]
        elif idx == length -1:
            prefixnum = prefix[idx -1]
            postfixnum = 1
        else:
            prefixnum = prefix[idx -1]
            postfixnum = postfix[idx + 1]
        staging_list.append(prefixnum * postfixnum)   
    print(staging_list) 
    return staging_list

def productExceptSelf_noextramemory(nums: list[int]) -> list[int]:
    length = len(nums)
    staging_list = [1] * length
    product_post = 1, 1
    if len(nums) < 1:
        return [-1]
       
    for i in range(1, length):
        staging_list[i] = staging_list[i-1] * nums[i -1]
    
    for i in range(length -1, -1, -1):
        staging_list[i] *= product_post
        product_post *= nums[i]
    
    return staging_list

class TestproductExceptSelf(unittest.TestCase):
    def test_productExceptSelf(self):
        test_data = [
            {'input': [1,2,4,6], 'expected': [48,24,12,8]},
            {'input': [-1,0,1,2,3], 'expected': [0,-6,0,0,0]},    
            {'input': [1,2,3,4], 'expected': [24,12,8,6]},        
            {'input': [-1,1,0,-3,3], 'expected': [0,0,9,0,0]},    
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = productExceptSelf_noextramemory(nums=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for Test Data: {test_case}. Got {actual} wheres expected: {expected}")

if __name__ == "__main__":
    unittest.main()
