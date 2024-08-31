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

def twoSum_using_n2(nums: list[int], target: int) -> list[int]:
    print(f"Loop with {nums}")
    for index, number in enumerate(nums):        
        for i in range(index + 1, len(nums)):
            print(f"Numbers are {number} and {nums[i]}")
            if number + nums[i] == target:
                return [index, i]
    return [-1]

def twoSum_using_hashmap(nums: list[int], target: int) -> list[int]:
    print(f"Loop with {nums}")   
    # temp_hashmap = {(k, v) for k, v in enumerate(nums)}
    # print(temp_hashmap)
    temp_hashmap = {} # val : index
    for index, number in enumerate(nums):
        diff = target - number
        if diff in temp_hashmap.keys():
            return [temp_hashmap[diff], index]
        temp_hashmap[number] = index
    
    return [-1]


class TestTwoSums(unittest.TestCase):
    def test_twosums(self):
        test_data = [
            {'input': [[3, 4, 5, 6], 7], 'expected': [0,1]},
            {'input': [[4,5,6], 10], 'expected': [0,2]},
            {'input': [[2,7,11,15], 9], 'expected': [0,1]},
            {'input': [[2,1,5,3], 4], 'expected': [1,3]},
            {'input': [[2,1,5,3], 10], 'expected': [-1]},
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = twoSum_using_hashmap(nums=test_case['input'][0], target=int(test_case['input'][1]))
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Expected {expected} but got in actual {actual}")

if __name__ == "__main__":
    unittest.main()
        
