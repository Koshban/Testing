'''
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)

'''
import unittest

def pair_product(pairs: list[int], target: int) -> list[int]:
    nums_hashmap = {}
    for idx, num in enumerate(pairs):
        complement = target/num
        if complement in nums_hashmap.keys():
            return [nums_hashmap[complement], idx]
        nums_hashmap[num] = idx
    return [-1]

class TestPairProduct(unittest.TestCase):
    def test_pair_product(self):
        test_data = [
            {'input': [[3, 2, 5, 4, 1], 8], 'expected': [1, 3]},
            {'input': [[3, 2, 5, 4, 1], 10], 'expected': [1, 2]},
            {'input': [[4, 7, 9, 2, 5, 1], 5], 'expected': [4, 5]},
               ]

        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = pair_product(pairs=test_case['input'][0], target=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Expected {expected} but got in actual {actual}")

if __name__ == "__main__":
    unittest.main()
