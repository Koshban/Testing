"""
**String Compression:**
    Implement a method to perform basic string compression using the counts of repeated characters. For example, the string `aabcccccaaa` would become `a2b1c5a3`. 
    If the "compressed" string does not become smaller than the original string, your method should return the original string
The string compression method iterates over the input string and counts the occurrences of each character. It builds a new "compressed" string by appending each character followed by its count. After processing the entire input string, the method compares the length of the compressed string with the original string:

If the compressed string is shorter, it is returned as the result.
If the compressed string is not shorter, the original string is returned, since the compression did not reduce the size.
Here are some notes on the example data and expected behavior:

('aabcccccaaa', 'a2b1c5a3'): This is the example given in the prompt, with a clear compression.
('abcd', 'abcd'): Each character appears only once, so compression would not make the string shorter.
('aaabbb', 'a3b3'): Each character appears multiple times, compression is effective.
('aabbcc', 'aabbcc'): Each character appears twice, so the compressed string would be the same length as the original and therefore ineffective.
('aaaaaffffcc', 'a5f4c2'): Characters appear in groups, and the counts are more than one digit, which shows that the function should handle multi-digit counts correctly.
('a', 'a'): A single character does not need compression.
('', ''): An empty string has nothing to compress.
('aaAAbBB', 'aaAAbBB'): Characters are case-sensitive, so 'a' and 'A' are treated differently, and compression is not effective.
('222555444', '23252534'): The function should work for strings containing digits, treating them as characters.
('abbcccddddeeeee', 'a1b2c3d4e5'): A string with varying counts, effectively compressed.
The function should preserve the original order of characters and be case-sensitive. It should also handle strings that contain digits as characters.
"""
import unittest
from collections import OrderedDict
def string_compression_to_count(string: str) -> str:
    if string is None:
        return string
    string_dict = OrderedDict()
    temp_list = []
    for s in string:
        string_dict[s] = string_dict.get(s, 0) + 1
    print(string_dict)
    for k, v in string_dict.items():
        temp_list.extend([k,v])
    print(temp_list)
    mystring = ''.join(str(item) for item in temp_list)
    print(mystring)
    return mystring

def string_compression(string: str) -> str:
    if string is None:
        return string
    
    compressed, count = [], 1
    for i in range(1, len(string)):
        if string[i] == string[i -1]:
            count += 1
        else:
            compressed.append(string[i -1] + str(count))
    compressed.append(string[-1] + str(count))
    comp_string = ''.join(compressed)
    return comp_string if len(comp_string) < len(string) else string

class TestStringCompression(unittest.TestCase):

    def test_string_compression(self):
        test_data = [
            ('aabcccccaaa', 'a2b1c5a3'),  # Basic example, compression is effective
            ('abcd', 'abcd'), 
                    ]            # No compression because it would not be shorter
            # ('aaabbb', 'a3b3'),           # Compression with multiple characters
            # ('aabbcc', 'aabbcc'),         # No compression, as it would not be shorter
            # ('aaaaaffffcc', 'a5f4c2'),    # Compression with some characters having more than one digit counts
            # ('a', 'a'),                   # Single character, no compression needed
            # ('', ''),                     # Empty string, nothing to compress
            # ('aaAAbBB', 'aaAAbBB'),       # Mixed case, should be treated as different characters and not compress
            # ('222555444', '23252534'),    # Numeric string compression
            # ('abbcccddddeeeee', 'a1b2c3d4e5') # Mixed counts, all compressible
            # ]
        for string, expected in test_data:
            with self.subTest(input=string, result=expected):
                actual_result = string_compression(string=string)
                self.assertEqual(actual_result, expected)

if __name__ == "__main__":
    unittest.main()
