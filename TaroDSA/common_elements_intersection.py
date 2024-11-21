'''
Write a function, intersection, that takes in two lists, a,_b_, as arguments. The function should return a new list containing elements that are in both of the two lists.
You may assume that each input list does not contain duplicate elements.
intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([2,4,6], [4,2]) # -> [2,4]
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
'''
import unittest

def common_elements(input_lists: list[list]) -> list[int]:
    if len(input_lists) != 2:
        return [ 0, 0]
    list_a = input_lists[0]
    list_b = input_lists[1]
    common_data = []
    set_a = set(list_a)
    print(set_a)
    for item in list_b:
        if item in set_a:
            common_data.append(item)
    #return common_data
    return [ele for ele in list_b if ele in set_a]

class TestCommonElements(unittest.TestCase):
    def test_common_elements(self):
        test_data =  [
            {'input': [[4,2,1,6], [3,6,9,2,10]], 'expected': [6, 2]},
            {'input': [[2,4,6], [4,2]], 'expected': [4, 2]},
            {'input': [[4,2,1], [1,2,4,6]], 'expected': [1,2,4]},
            {'input': [[4,2,1]], 'expected': [0, 0]},
               ]
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                actual = common_elements(input_lists=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Expected {expected} but got in actual {actual}")

if __name__ == "__main__":
    unittest.main()