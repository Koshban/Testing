'''Squares of a list of numbers in place and out of place'''
import unittest

def squares_in_place(int_list: list[int]) -> list[int]:
    for index, element in enumerate(int_list):
        int_list[index] *= element
    return int_list


def squares_out_of_place(int_list: list[int]) -> list[int]:
    final_list = [0] * len(int_list)
    for index, element in enumerate(int_list):
        final_list[index] = element * element
    return final_list



class TestSquares(unittest.TestCase):
    def test_squares(self):
        test_data = [
            {'input': [2, 3, 4, 5], 'expected': [4, 9, 16, 25]},
        ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = squares_out_of_place(int_list=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case['input']}. Expected {expected} but received {actual}.")

if __name__ == "__main__":
    unittest.main()




