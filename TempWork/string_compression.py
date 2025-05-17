'''
    Implement a method to perform basic string compression using the counts of repeated characters. For example, the string `aabcccccaaa` would become `a2b1c5a3`. If the "compressed" string 
    does not become smaller than the original string, your method should return the original string.
'''
import unittest

def compress_string(s: str) -> str:
    if not s:
        return ""
    result = []
    current = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            result.append(current + str(count))
            current = s[i]
            count = 1
    result.append(current + str(count))
    result = ''.join(result)

    return result if len(result) < len(s) else s   


class TestStringCompression(unittest.TestCase):
    def test_string_compression(self):
        test_data = [
            {'input': "aabcccccaaa", 'expected': "a2b1c5a3"},
            {'input': "abc", 'expected': "abc"},  # Return original if compressed isn't smaller
            {'input': "aabb", 'expected': "aabb"},  # Return original if compressed isn't smaller
            {'input': "aabbaabb", 'expected': "aabbaabb"},
            {'input': "abcdef", 'expected': "abcdef"},
            {'input': "aaa", 'expected': "a3"},
            {'input': "a", 'expected': "a"},
            {'input': "", 'expected': ""},
            {'input': "AABBCC", 'expected': "AABBCC"},
            {'input': "aaAAaa", 'expected': "aaAAaa"},
            {'input': "aaaabbbccc", 'expected': "a4b3c3"},
            {'input': "aaaaaaaaa", 'expected': "a9"},
            {'input': "aabbaaccaa", 'expected': "aabbaaccaa"},
            {'input': "abcabcabc", 'expected': "abcabcabc"},
            {'input': "aabbccddee", 'expected': "aabbccddee"},
            {'input': "aaabbaabbb", 'expected': "a3b2a2b3"},
            {'input': "abcdefabc", 'expected': "abcdefabc"},
            {'input': "aaabbbcccaaa", 'expected': "a3b3c3a3"},
            {'input': "aaaaabbbbb", 'expected': "a5b5"},
            {'input': "    ", 'expected': " 4"}  # Handle spaces
         ]
        
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = compress_string(test_case["input"])
                expected = test_case["expected"]
                self.assertEqual(actual, expected, 
                               f"Failed for {test_case}. Actual {actual} but expected {expected}")

if __name__ == "__main__":
    unittest.main()

