"""
Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string. The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.
Constraints:
Let s be the expression string. We can assume the following constraints:
    1 ≤ s.length ≤ 3×10^4
    s consists of digits, “+”, “-”, “(”, and “)”.
    s represents a valid expression.
    “+” is not used as a unary operation 
    “-” could be used as a unary operation
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
import unittest

def basic_calculator(input: str) -> int:
    stack = []
    temp_result, num = 0, 0
    signvalue = 1 # Assume positive value by default
    for s in input:
        print(s)
        if s.isdigit():
            num = num * 10 + int(s)
            print(f"Num here is {num}")
        elif s in '+-':
            temp_result += num * signvalue
            signvalue = -1 if s == '-' else 1
            num = 0
        elif s == '(':
            stack.append(temp_result)
            stack.append(signvalue)
            temp_result = 0
            signvalue = 1        
        elif s == ')':
            temp_result += signvalue * num
            pop_sign_value = stack.pop()
            temp_result *= pop_sign_value 

            second_value = stack.pop()
            temp_result += second_value
            num = 0
    return temp_result + num * signvalue

class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        test_data = [
                ("1+1", 2),
                ("(1+(4+5+2)-3)+(6+8)", 23),
                ("1+(4+5+2)-3+(6+8)-11", 12),
                ("((2+13)+(1+28))", 44),
                ("-1+(-2-3)", -6),
                ("1-(--2+3)", 0),
                (" 1 + 1 ", 2),
                ("((((3))))", 3),
                ("", 0)  # Assuming the calculator function returns 0 for an empty string
            ]
        for expression, expected in test_data:
            with self.subTest(input=expression, output=expected):
                result = basic_calculator(input=expression)
                self.assertEqual(result, expected), f"Test Failed for {expression}. Got : {result} whereas expected : {expected}"


if __name__ == "__main__":
    unittest.main()
    print(basic_calculator(input="-1+(-32-3)"))

