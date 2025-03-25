'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.
Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
'''
import unittest

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #left, right = 0, len(numbers) - 1
        nums_hashmap, answer = {}, []
        for index, num in enumerate(numbers):
            find_num = target - num
            #left, right, middle = index + 1, len(numbers) -1, (left + right)/2
            print(f"Num is {num} at Index : {index}. Diff is {find_num}")
            if find_num in nums_hashmap.keys():
                print(f"Hashmap is {nums_hashmap}")
                second_num = nums_hashmap[find_num] + 1
                answer = [second_num, index + 1  ]
                return answer
            nums_hashmap[num] = index
            print(f"Hashmap Outside is {nums_hashmap}")        


class TestTwoSum(unittest.TestCase):
    def test_is_two_sum(self):
        test_data = [
    {'input': {'numbers': [1, 2, 3, 4], 'target': 3}, 'expected': [1, 2]},  # Basic case
    {'input': {'numbers': [2, 7, 11, 15], 'target': 9}, 'expected': [1, 2]},  # Classic example
    {'input': {'numbers': [-3, -1, 0, 1, 3], 'target': -1}, 'expected': [2, 3]},  # Negative numbers
    {'input': {'numbers': [1, 2, 3, 4, 5, 6], 'target': 11}, 'expected': [5, 6]},  # Numbers at the end
    {'input': {'numbers': [1, 2, 3, 4, 5, 8, 10], 'target': 10}, 'expected': [2, 6]},  # Non-consecutive numbers
    {'input': {'numbers': [-10, -5, 0, 5, 10], 'target': 0}, 'expected': [2, 4]},  # Mixed negative and positive numbers
    {'input': {'numbers': [1, 3, 5, 7, 9, 11], 'target': 16}, 'expected': [4, 5]},  # Odd numbers
    {'input': {'numbers': [2, 4, 6, 8, 10, 12], 'target': 14}, 'expected': [3, 4]},  # Even numbers
    {'input': {'numbers': [-3, -2, -1, 0, 1], 'target': -4}, 'expected': [1, 3]},  # All negative numbers
    {'input': {'numbers': [1, 2], 'target': 3}, 'expected': [1, 2]},  # Minimal input size
    {'input': {'numbers': [1, 2, 4, 8, 16, 32], 'target': 36}, 'expected': [3, 6]},  # Larger powers of two
    {'input': {'numbers': [10, 20, 30, 40], 'target': 50}, 'expected': [2, 3]},  # Numbers with larger gaps
    {'input': {'numbers': [-10, -5, -2, 0, 3, 7], 'target': -12}, 'expected': [1, 3]},  # Negative target
    {'input': {'numbers': [1, 1, 1, 1, 1, 1, 1, 1, 1], 'target': 2}, 'expected': [1, 2]},  # Repeated single number
]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                print(test_case["input"]["numbers"])
                print(test_case["input"]["target"])
                print(test_case["expected"])
                actual = solution.twoSum(numbers=test_case["input"]["numbers"], target=test_case["input"]["target"])
                expected = test_case["expected"]
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()