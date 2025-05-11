'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.
Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25
'''
import unittest
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxnum = 0
        if len(piles) == 0 or len(piles) > h:
            return -1
        #print(piles)
        for num in piles:
            #print(f"Num is {num}")
            maxnum = max(maxnum, num)
        #print(maxnum)
        if len(piles) == h:
            return maxnum
        
        maxnumrange = [i for i in range(1, maxnum + 1)]
        print(maxnumrange)
        l, r, res = 0, len(maxnumrange) -1, maxnum
        while l <= r:
            m = (l + r )//2
            hours_taken = [math.ceil(x//m) for x in piles]
            print(f"1. Hours is {hours_taken}")
            hours = sum(hours_taken)
            if hours < h:
                r = m -1
                res = min(res, m)
            else:
                l = m + 1
        return res

class TestminEatingSpeed(unittest.TestCase):
    def test_minEatingSpeed(self):
        test_data = [
                {'input': ([1,4,3,2], 9), 'expected': 2},
                {'input': ([25,10,23,4], 4), 'expected': 25},
                {'input': ([1,3,5,7], 3), 'expected': -1},
                {'input': ([], 8), 'expected': -1}, 
                
            ]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                #print(f"in Test : Matrix is {test_case['input'][0]}")
                actual = solution.minEatingSpeed(piles=test_case['input'][0], h=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()