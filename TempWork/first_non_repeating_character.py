'''
Given a string, write a function to find the first non-repeating character in the string and return its index. If there are no non-repeating characters, return -1.
'''
import unittest
class Solution:
    def first_unique(self, inputstring: str) -> int:
        stagingtable = {}
        inputstring = inputstring.replace(' ','')
        if len(inputstring) == 0:
            return -1
        for index, char in enumerate(inputstring):
            if char in stagingtable.keys():
                stagingtable[char] += 1
            else:
                stagingtable[char] = 1
        
        for index, char in enumerate(inputstring):
            if stagingtable[char] == 1:
                return index
        
        return -1

class TestFirstUnique(unittest.TestCase):
    def test_first_unique(self):
        test_data = [            
            {'input': "leetcode", 'expected': 0},  # 'l' is first non-repeating
            {'input': "loveleetcode", 'expected': 2},  # 'v' is first non-repeating
            {'input': "aabb", 'expected': -1},  # no non-repeating characters
            {'input': "", 'expected': -1},  # empty string
            {'input': "aaa", 'expected': -1},  # all repeating
            {'input': "z", 'expected': 0},  # single character
            {'input': "dddccdbba", 'expected': 8},  # 'a' at the end
            {'input': "abcdefg", 'expected': 0},  # all unique characters
            {'input': "aadadaad", 'expected': -1},  # multiple repeating
            {'input': "   ", 'expected': -1},  # all spaces
        ]
 
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.first_unique(inputstring=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()