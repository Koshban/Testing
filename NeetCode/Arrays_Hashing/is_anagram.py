'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true

Input: s = "jar", t = "jam"
Output: false
'''
import unittest
import re
from collections import Counter

def is_anagram_using_sorted(t:str, s: str) -> bool:
    t = re.sub(r'[^a-zA-Z]','', t)
    s = re.sub(r'[^a-zA-Z]','', s)
    return sorted(t) == sorted(s)

def is_anagram_using_counter(t:str, s: str) -> bool:
    t = re.sub(r'[^a-zA-Z]','', t)
    s = re.sub(r'[^a-zA-Z]','', s)
    return Counter(t) == Counter(s)

def is_anagram_using_hashmap(t:str, s: str) -> bool:
    t = re.sub(r'[^a-zA-Z]','', t)
    s = re.sub(r'[^a-zA-Z]','', s)
    dict_t, dict_s = {}, {}
    if len(t) == len(s):
        for i in t:
            if i in dict_t.keys():
                dict_t[i] += 1
            dict_t[i] = 1
        
        for j in s:
            print(f"J is {j}")
            if j in dict_s.keys():
                dict_s[j] += 1
            dict_s[j] = 1
        print(f" DT is {dict_t} and DS is {dict_s}. S is {s}")
        if dict_s == dict_t:
            return True
    return False

class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        test_data = [
    ({'input': ["listen", "silent"], 'expected': True}),
    ({'input': ["triangle", "integral"], 'expected': True}),
    ({'input': ["hello", "billion"], 'expected': False}),
    ({'input': ["dormitory", "dirty room"], 'expected': True}),
    ({'input': ["conversation", "voices rant on"], 'expected': True}),
    ({'input': ["a gentleman", "elegant man"], 'expected': True}),
    ({'input': ["schoolmaster", "the classroom"], 'expected': True}),
    ({'input': ["punishments", "nine thumps"], 'expected': False}),
    ({'input': ["astronomer", "moon starer"], 'expected': True}),
    ({'input': ["debit card", "bad credit"], 'expected': True}),
    ({'input': ["ddogg", "god"], 'expected': False}),
    ({'input': ["odg", "god"], 'expected': True}),
    ({'input': ["race", "care"], 'expected': True}),
    ({'input': ["stop", "tops"], 'expected': True}),
    ({'input': ["earth", "heart"], 'expected': True})
]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = is_anagram_using_counter(t=test_case["input"][0], s=test_case["input"][1])
                expected = test_case["expected"]
                self.assertEqual(actual, expected, f" Failed for {test_case}. Actual {actual} but expected {expected}")

if __name__ == "__main__":
    unittest.main()