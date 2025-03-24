'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
'''
import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        if len(s) == 0:
            return False
        for char in s:
            if char.isalnum():
                newstr += char.lower()
        if not newstr:
            return False # To catch empty strings
        return newstr == newstr[::-1] 
    
class Solution_new:   
    
    def isPalindrome(self, s: str) ->bool:
        l, r = 0, len(s) - 1
        # Check if the string contains no alphanumeric characters
        if all(not self.isAlphaNum(c) for c in s):
            return False
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def isAlphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') 
            )
    
    
class TestIsPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        test_data = [
    {'input': "racecar", 'expected': True},  # Basic palindrome
    {'input': "hello", 'expected': False},  # Not a palindrome
    {'input': "A man a plan a canal Panama", 'expected': True},  # Palindrome with spaces and case differences
    {'input': "No lemon, no melon", 'expected': True},  # Palindrome with punctuation and spaces
    {'input': "12321", 'expected': True},  # Numeric palindrome
    {'input': "12345", 'expected': False},  # Non-palindromic number
    {'input': "", 'expected': False},  # Empty string (not considered a palindrome)
    {'input': "a", 'expected': True},  # Single character string
    {'input': "aa", 'expected': True},  # Two identical characters
    {'input': "ab", 'expected': False},  # Two different characters
    {'input': "Able was I ere I saw Elba", 'expected': True},  # Famous palindrome phrase
    {'input': "Was it a car or a cat I saw?", 'expected': True},  # Palindrome with a question mark
    {'input': "Madam, in Eden, I'm Adam", 'expected': True},  # Palindrome with apostrophe and punctuation
    {'input': "Step on no pets", 'expected': True},  # Simple palindrome with spaces
    {'input': " ", 'expected': False},  # Single space (not a palindrome)
    {'input': "1234321", 'expected': True},  # Long numeric palindrome
    {'input': "12344321", 'expected': True},  # Even length numeric palindrome
    {'input': "palindrome", 'expected': False},  # Completely unrelated string
]
        solution = Solution_new()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.isPalindrome(s=test_case["input"])
                expected = test_case["expected"]
                print(f"Running test Case: {test_case}")
                self.assertEqual(actual, expected, f"Failed for {test_case["input"]}. Received : {actual} , was expecting : {expected}")

    

if __name__ == "__main__":
    unittest.main()



