''' Write a function to check if a string is a palindrome (reads the same forwards and backward) without using any extra space. '''
import unittest

def is_palindrome(stringtocheck: str) -> bool:
    jointstring = ''.join(c.lower() for c in stringtocheck if c.isalnum())
    return jointstring == jointstring[::-1]

class Testis_palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        test_data = [
            ("racecar", True),
            ("", True),
            ("a", True),
            ("hello", False),
            ("A man a plan a canal Panama", True),
            ("race a car", False),
            ("12321", True),
            ("Was it a car or a cat I saw", True),
            ("12345", False),
            ("Madam Im Adam", True),
            ("Never odd or even", True),
            ("hello world", False),
            ("Do geese see God", True),
            ("ab", False),
            ("aba", True),
            ("Mr Owl ate my metal worm", True),  # Corrected to True
            ("Sit on a potato pan Otis", True),
            ("123", False),
            ("1221", True),
            ("x", True)
        ]
        for string, expected in test_data:
            with self.subTest(input=string, expected=expected):
                actual = is_palindrome(stringtocheck=string)
                expected=expected
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()