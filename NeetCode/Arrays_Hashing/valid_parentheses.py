'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false as The brackets are not closed in the correct order.

'''
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack, stagingtable = list(s), []
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
        
        for element in temp_stack:
            if element in ref_dict.keys():
                stagingtable.append(element)
            elif element in rev_ref_data.keys():
                if stagingtable:
                    comp_element = stagingtable.pop()
                    if rev_ref_data[element] != comp_element:
                        return False   
                else:
                    return False         
            else:
                return False
        return False if stagingtable else True


class testisValid(unittest.TestCase):
    def test_isValid(self):
        solution = Solution()
        test_data = [
            {'input': "[]", 'expected': True},
            {'input': "([{}])", 'expected': True},         
            {'input': "[(])", 'expected': False},   
            {'input': "[]()[]()", 'expected': True},   
            {'input': "[]()[(){", 'expected': False}, 
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = solution.isValid(s=test_case['input'])
                expected=test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()