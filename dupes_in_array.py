"""
**Find All Duplicates in an Array:**
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of an array), some elements appear twice and others appear once. Find all the elements that appear twice in this array. Could you do it without extra space and in O(n) runtime?
nums = [4, 3, 2, 7, 8, 2, 3, 1]
Better still find count of each element
   """
import unittest

def find_duplicate_nums_using_array(input: list) -> list:
    if len(input) == 0:
        return []
    staging_area = {}
    for element in input:
        staging_area[element] = staging_area.get(element, 0) + 1
    # Filter out the elements with count =1
    final_counts = {element: count for element, count in staging_area.items() if count > 1}
    print(f"\t\t{final_counts}")
    final_count_list = sorted([element for element in final_counts.keys()])
    print(f"\t{final_count_list}")
    return final_count_list

class TestFIndDupes(unittest.TestCase):
    def test_find_duplicate_nums_using_array(self):
        test_data = [
            ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], [1]),
            ([10, 22, 10, 20, 11, 22, 33, 44, 55, 33], [10, 22, 33]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 9], [9]),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5]),
            ([2, 3, 7, 6, 2, 3, 1, 1, 5], [2, 3, 1]),
            ([], []),
            ([1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4]),
            ([8, 9, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8], [9, 8]),
            ([15, 16, 15, 17, 18, 19, 16, 16], [15, 16]),
            ([21, 22, 23, 24, 25, 21, 24], [21, 24]),
            ([31, 32, 33, 34, 35, 36, 37, 38, 39, 31, 37, 39], [31, 37, 39]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 2], [6, 2]),
            ([10, 11, 12, 11, 13, 14, 15, 16, 17, 10], [11, 10]),
            ([45, 45, 46, 47, 46, 48, 49], [45, 46]),
            ([4, -3, 2, 7, 8, 2, -3, 1, 4], [4, 2, -3]),
            (['a', 'b', 'c', 'a', 'd', 'c'], ['c', 'a'])
            ]
        for data, expected in test_data:
            with self.subTest(input=data, expected=expected):
                result_sorted = sorted(expected)
                self.assertEqual(find_duplicate_nums_using_array(input=data), result_sorted) 

if __name__ == "__main__":
    # test_data = [
    # ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], [1]),
    # ([10, 22, 10, 20, 11, 22, 33, 44, 55, 33], [10, 22, 33]),
    # ([9, 8, 7, 6, 5, 4, 3, 2, 1, 9], [9]),
    # ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5]),
    # ([2, 3, 7, 6, 2, 3, 1, 1, 5], [2, 3, 1]),
    # ([], []),
    # ([1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4]),
    # ([8, 9, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8], [9, 8]),
    # ([15, 16, 15, 17, 18, 19, 16, 16], [15, 16]),
    # ([21, 22, 23, 24, 25, 21, 24], [21, 24]),
    # ([31, 32, 33, 34, 35, 36, 37, 38, 39, 31, 37, 39], [31, 37, 39]),
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 2], [6, 2]),
    # ([10, 11, 12, 11, 13, 14, 15, 16, 17, 10], [11, 10]),
    # ([45, 45, 46, 47, 46, 48, 49], [45, 46])
    # ]
    # for data, result in test_data:
    #     find_duplicate_nums_using_array(input=data)
    unittest.main()