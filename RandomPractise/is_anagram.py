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

def is_anagram_using_sorted(t:str, s:str) -> bool:
    #Remove all non Letter ([^a-zA-z] characters like spaces ' etc by replacing them with nothing ('')
    t = re.sub(r'[^a-zA-Z]', '', t)
    s = re.sub(r'[^a-zA-Z]', '', s)
    return sorted(t) == sorted(s)

def is_anagram_using_counters(t:str, s:str) -> bool:
    t= re.sub(r'[^a-zA-Z]', '', t)
    s = re.sub(r'[^a-zA-Z]', '', s)
    return Counter(t) == Counter(s)

def is_anagram_using_hashmap(t:str, s: str) -> bool:
    t = re.sub(r'[^a-zA-Z]','', t)
    s = re.sub(r'[^a-zA-Z]','', s)
    dict_t, dict_s = {}, {}

    for letter_t in t:
        if letter_t in dict_t.keys():
            dict_t[letter_t] += 1
        else:
            dict_t[letter_t] = 1
    print(f"T Letter is {letter_t} and T dict is {dict_t}")
    
    for letter_s in s:
        if letter_s in dict_s.keys():
            dict_s[letter_s] += 1
        else:
            dict_s[letter_s] = 1
    print(f"S Letter is {letter_s} and S dict is {dict_s}")
    
    return dict_s == dict_t

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
    ({'input': ["earth", "heart"], 'expected': True}),
    ({'input': ["cats", "tocs"], 'expected': False}),
    ({'input': ["paper", "reapa"], 'expected': False}),
    ({'input': ["monkeyswrite", "newyorktimes"], 'expected': True}),
    ({'input': ["restful", "fluster"], 'expected': True})
]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = is_anagram_using_hashmap(t=test_case["input"][0], s=test_case["input"][1])
                expected = test_case["expected"]
                self.assertEqual(actual, expected, f" Failed for {test_case}. Actual {actual} but expected {expected}")

if __name__ == "__main__":
    unittest.main()