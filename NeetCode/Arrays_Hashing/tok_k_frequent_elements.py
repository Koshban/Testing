'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]
'''
import unittest

def topKFrequent_mine(nums : list[int], k: int) -> list[int]:
    temp_hash, count, final_list = {}, 0, []
    print(f"Nums : {nums}. K :{k}")
    if len(nums) < 1:
        return [-1]
    for number in nums:
        if number in temp_hash.keys():
            temp_hash[number] += 1
        else:
            temp_hash[number] = 1
    print(f"temp_hash is {temp_hash}")
    sorted_hash = dict(sorted(temp_hash.items(), key = lambda item: item[1], reverse=True))
    print(sorted_hash)
    for key in sorted_hash.keys():
        if count < k:
            final_list.append(key)
            count += 1
    return final_list

def topKFrequent(nums : list[int], k: int) -> list[int]:
    if len(nums) < 1:
        return [-1]
    count, result = {}, []
    frequency = [[] for i in range(len(nums) + 1)] # The Frequency List where index will be the count of occurences and the values will be a list of numbers with that number of occurences
    for number in nums:
        count[number] = 1 + count.get(number, 0)
        print(f"Count is {count}")
    print(f"Count.items is {count.items()}")
    for n, c in count.items():
        print(f" N is {n} and C is {c}")
        frequency[c].append(n) # The value N occurrs C number of times in the nums list
        print(f"Frequency is {frequency}")
    for i in range(len(frequency) -1, 0, -1):
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result

class TestFrequentElements(unittest.TestCase):
    def test_topKFrequent(self):
        test_data = [
            {'input': [[1,2,2,3,3,3], 2], 'expected': [3,2]},
            {'input': [[7,7], 1], 'expected': [7]},
            {'input': [[], 1], 'expected': [-1]}
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = topKFrequent(nums=test_case['input'][0], k = test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Got {actual} where was expecting {expected}")

if __name__ == "__main__":
    unittest.main()