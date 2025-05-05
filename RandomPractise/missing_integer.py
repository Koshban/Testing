"""
Missing Number in Sequence:**
Given a list of `n-1` integers in the range from 1 to `n`, there’s no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.

"""

import random
import unittest

def generate_test_data(n : int, seed : int=None) -> list:
    if seed is not None:
        random.seed(seed) # Seed for reproducability, useful for PRNGS and for repetitive unittests
    if not (isinstance(n, int) and isinstance(seed, int)):
        print(f"INT is {type(n)} and seed is {type(seed)}")
        print("Incorrect Type. Should be INTEGER")
        return [-1]
    
    # Craete the Range
    full_list = list(range(1, n + 1))
    #Remove one number
    remove_num = random.choice(full_list)

    full_list.remove(remove_num)
    random.shuffle(full_list)

    return full_list, remove_num

def find_missing_number(inputdata : list, n: int) -> int:
    print(f"Input Data is {inputdata}")
    idealsum = n * (n +1)//2
    missingnum = idealsum - sum(inputdata)
    return missingnum


class TestMissingNum(unittest.TestCase):
    # def test_generate_test_data(self):
    #     seed, n = 42, 200
    #     test_data, missing_number = generate_test_data(n=n, seed=seed)
    #     self.assertEqual(len(test_data), n-1)
    #     self.assertIn(missing_number, range(1, n +1))

    def test_find_missing_number(self):
        seed, n = 42, 200
        test_data, missing_number = generate_test_data(n=n, seed=seed)
        found_missingnum = find_missing_number(inputdata=test_data, n=n)
        self.assertEqual(missing_number, found_missingnum)

if __name__ == "__main__":
    n = 30
    ourlist, missingnumber = generate_test_data(n=n, seed=5)
    foundnum = find_missing_number(inputdata=ourlist, n=n)
    print(f"\tFrom the List \t\t{ourlist}")
    print(f"\t\t\t{foundnum} is MISSING")
    unittest.main()


