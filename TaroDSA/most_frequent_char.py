'''
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.
You can assume that the input string is non-empty.
most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'
most_frequent_char('abby') # -> 'b'
most_frequent_char('mississippi') # -> 'i'

'''

import unittest
from collections import Counter

def using_counters(word: str) -> int:
    counter_word = Counter(word)
    max_frequency = 0
    #counter_word = dict(sorted(counter_word.items(), key=lambda item: item[1]))
    for chars in word:
        frequency = counter_word[chars]
        if frequency > max_frequency:
            max_frequency = frequency
            character_with_max_frequency = chars
    return character_with_max_frequency

def using_hashmaps(word: str) -> int:
    dict_word, max_frequency = {}, 0
    for chars in word:
        if chars in dict_word.keys():
            dict_word[chars] += 1
        else:
            dict_word[chars] = 1
    
    for chars in word:
        frequency = dict_word[chars]
        if frequency > max_frequency:
            max_frequency = frequency
            character_with_max_frequency = chars
    return character_with_max_frequency     

class TestMostFrequent(unittest.TestCase):
    def test_most_frequent_char(self):
        test_data = [
    ({'input': "bookeeper", 'expected': 'e'}),
    ({'input': "david", 'expected': 'd'}),
    ({'input': "abby", 'expected': 'b'}),
    ({'input': "mississippi", 'expected': 'i'})]
        #print(f"test data is {test_data}")
        for test_case in test_data:
            #print(f"Test Case is {test_case}")
            with self.subTest(test_case=test_case):
                actual = using_hashmaps(word=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f" Failed for {test_case}. Actual {actual} but expected {expected}")


if __name__ == '__main__':
    unittest.main()

                 

