'''
Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all the numbers in the array. All elements will be integers. Solve this recursively.

sum_numbers_recursive([5, 2, 9, 10]); # -> 26
sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]); # -> 1
sum_numbers_recursive([]); # -> 0
sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]); # -> 1001
'''
import unittest

def sum_numbers(numberlist: list[int], sum: int = 0) -> int:
    if len(numberlist) == 0:
        return sum
    sum += numberlist[-1]
    numberlist.pop()
    print(f"Sum is {sum} and List is now {numberlist}")
    return sum_numbers(numberlist=numberlist, sum=sum)

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        test_data =  [
            {'input': [5, 2, 9, 10], 'expected': 26},
            {'input': [1, -1, 1, -1, 1, -1, 1], 'expected': 1},
            {'input': [], 'expected': 0},
            {'input': [1000, 0, 0, 0, 0, 0, 1], 'expected': 1001},
               ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = sum_numbers(numberlist=test_case['input'])
                print(f"Actual is {actual} and List is now {test_case['input']}")
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()