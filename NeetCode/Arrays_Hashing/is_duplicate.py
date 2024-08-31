'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
Input: nums = [1, 2, 3, 3]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false
'''
import unittest

def is_duplicate_using_dict(nums: list[int]) -> bool:
    if len(nums) < 2:
        return False
    print(nums)
    temp_dict = {}
    for num in nums:
        if num in temp_dict.keys():
            temp_dict[num] += 1
            return True
        temp_dict[num] = 1
    # temp_dict_sorted = dict(sorted(temp_dict.items(), key = lambda item:item[0], reverse=True))
    return False

def is_duplicate_using_sets(nums: list[int]) -> bool:
    if len(nums) < 2:
        return False
    return len(set(nums)) != len(nums)


class TestIsDuplictae(unittest.TestCase):
    def test_is_duplicate(self):
        test_data = [
            {'input': [1, 2, 3, 3], 'expected': True},
            {'input': [1, 2, 3, 4], 'expected': False},
            {'input': [1,1,1,3,3,4,3,2,4,2,2, 3, 3], 'expected': True},
            {'input': [], 'expected': False},
        ]

        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = is_duplicate_using_sets(nums=test_case['input'])
                expected = test_case['expected']
                print(f"Running for {test_case}")
                self.assertEqual(actual, expected, f"Failed for {test_case["input"]}, Got {actual} but was expecting {expected}")

if __name__ == "__main__":
    unittest.main()