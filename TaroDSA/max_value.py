'''
Write a function, max_value, that takes in a list of numbers as an argument. The function should return the largest number in the list.
Solve this without using any built-in list methods.
You can assume that the list is non-empty.
max_value([4, 7, 2, 8, 10, 9]) # -> 10
max_value([10, 5, 40, 40.3]) # -> 40.3
max_value([-5, -2, -1, -11]) # -> -1
'''
import unittest

''' time = O(n) and Space = O(1)'''
def max_value(group: list) -> int:
    maximum = float('-inf')
    if len(group) == 0:
        return 0.00
    for idx, num in enumerate(group):
        maximum = max(maximum, num)
    return maximum

class Testmaxvalue(unittest.TestCase):
    def test_maxvalue(self):
        test_data = [
            {'input': [4, 7, 2, 8, 10, 9], 'expected': 10},
            {'input': [10, 5, 40, 40.3], 'expected': 40.3 },
            {'input': [-5, -2, -1, -11], 'expected': -1 },
            {'input': [], 'expected': 0.00}, 
        ]
    
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = max_value(group=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}.\nGot : {actual} while expecting : {expected}")

if __name__ == "__main__":
    unittest.main()
    