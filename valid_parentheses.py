"""
Given a string, s, that may have matched and unmatched parentheses, remove the minimum number of parentheses so that the resulting string represents a valid 
parenthesization. For example, the string “a(b)” represents a valid parenthesization while the string “a(b” doesn’t, since the opening parenthesis doesn’t 
have any corresponding closing parenthesis.

"""
import unittest

def balanced_paranthese(input: str) -> str:
    datacopy = list(input)
    comp_dict = { 
                ')':'(',
                '}':'{',
                ']':'['
                }
    stack = []
    input_list = list(input)
    for i, s in enumerate(input_list):
        # print(f"Index is {i} for element {s} and stack is {stack}")
        if s in comp_dict.keys():
            if stack and comp_dict[s] == stack[-1][0]:
                stack.pop()
            else:
                stack.append([s, i])
        elif s in comp_dict.values():
            stack.append([s, i])
    print(f"Final Stack is {stack}")
    for element in stack:
        datacopy[element[1]] = ""
    print(datacopy)
    return ''.join(datacopy)               


class TestParentheses(unittest.TestCase):
    def test_balanced_parentheses(self):
        test_cases = [
        ("abc", "abc"),  # No parentheses
        ("a(b)c", "a(b)c"),  # Matched parentheses
        ("a(b(c", "abc"),  # Unmatched opening parenthesis
        ("a(b)c)", "a(b)c"),  # Unmatched closing parenthesis
        ("a(b)c)d(e)f)g(h)i)j(k", "a(b)cd(e)fg(h)ijk"),  # Multiple unmatched
        ("a((b)c)d)e)f)g(h)i)j(k", "a((b)c)defg(h)ijk"),  # Nested unmatched
        ("a(b))c)d)e(f(g(h)i)j(k", "a(b)cdef(g(h)i)jk"),  # Consecutive unmatched
    ]
        for case, expected in test_cases:
            self.subTest(input=case, expected=expected)
            output = balanced_paranthese(input=case)
            self.assertEqual(output, expected), f"Failed for {case} as output from the Function was {output}"        

if __name__ == "__main__":
    unittest.main()
    print(balanced_paranthese(input="a(b))c)d)e(f(g(h)i)j(k"))

