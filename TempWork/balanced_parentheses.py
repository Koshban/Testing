'''
**Balanced Parentheses:**
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid and return a boolean. An input string is valid if the 
brackets are closed in the correct order.
'''
import unittest
import logging
import os

script_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{script_name}.log'),
        logging.StreamHandler()
    ]
)

def balanced_parentheses(s: str) -> bool:
    stagingtable = []
    ref_dict = {
            '{' : '}',
            '(' : ')',
            '[' : ']',
        }
    rev_ref_data = {
        '}' : '{',
        ')' : '(',
        ']' : '[',
    }

    for index, element in enumerate(s):
        logging.info(f"At Index: {index} we have {element}")
        if element in rev_ref_data.keys():
            if stagingtable:
                matching = stagingtable.pop()
                if rev_ref_data[element] != matching:
                    return False
            else:
                return False
        elif element in ref_dict.keys():
            stagingtable.append(element)
    return False if stagingtable else True

class testisValid(unittest.TestCase):
    def test_isValid(self):
        test_data = [
            {'input': "[]", 'expected': True},
            {'input': "([{}])", 'expected': True},         
            {'input': "[(])", 'expected': False},   
            {'input': "[]()[]()", 'expected': True},   
            {'input': "[]()[(){", 'expected': False}, 
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = balanced_parentheses(s=test_case['input'])
                expected=test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()