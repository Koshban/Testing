"""
**Anagram Detection:**
Write a function to determine if two given strings are anagrams of each other. An anagram is a word or phrase that is made by rearranging the letters of another word or phrase.
    
"""
import unittest


def find_anagrams(strings : list) -> bool:
    print(strings)
    if len(strings) == 2:
        try:
            string1, string2 = strings[0], strings[1]
            string1 = string1.replace(' ', '').lower()
            string2 = string2.replace(' ', '').lower()
            if sorted(string1) == sorted(string2):
                return True
            else:
                return False
        except Exception as e:
            print(f'Incorrect Input. Error Encountered {e}')
            return -1


    else:
        return -1, f'Incorrect Input length. Should be 2 words only'

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        test_data = [
            (["listen", "silent"], True),
            (["triangle", "integral"], True),
            (["hello", "billion"], False),
            (["dormitory", "dirty room"], True),
            (["conversation", "voices rant on"], True),
            (["a gentleman", "elegant man"], True),
            (["schoolmaster", "the classroom"], True),
            (["punishments", "nine thumps"], False),
            (["astronomer", "moon starer"], True),
            (["debit card", "bad credit"], True),
            (["ddogg", "god"], False),
            (["odg", "god"], True),
            (["race", "care"], True),
            (["stop", "tops"], True),
            (["earth", "heart"], True)
        ]
    
        for strings, expected in test_data:
            with self.subTest(input=strings,expected=expected):
                self.assertEqual(find_anagrams(strings=strings), expected)

if __name__ == "__main__":
    unittest.main()
