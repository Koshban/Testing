'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''
import unittest

def longest_common_subsequence(text1: str, text2: str) -> int:
    if len(text2) > len(text1):
       t1, t2 = text2, text1
       
    else:
        t1, t2 = text1, text2
        
    

class TestLongestCommonSubSequence(unittest.TestCase):
    def test_longest_common_subsequence(self):
        test_data = [
            {'input': ['abc', 'abc'], 'expected': 3},
            {'input': ['abcde', 'ace'], 'expected': 3},
            {'input': ['abcde', 'aeb'], 'expected': 2},
            {'input': ['abc', 'def'], 'expected': 0},
            {'input': ['cabde', 'bdecabe'], 'expected': 4}
        ]
        for test_case in test_data:        
            with self.subTest(test_case=test_case):
                text1, text2 = test_case["input"]
                expected =  test_case["expected"]
                actual = longest_common_subsequence(text1=text1, text2=text2)
                self.assertEqual(actual, expected, f"Failed for {test_case["input"]}, Got {actual} but was expecting {expected}")


if __name__ == "__main__":
    unittest.main()