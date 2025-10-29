"""
Applies range update operations to an array of zeros.
Write a function called apply_range_updates that takes an array size and a list of update operations, then applies all the updates to an initially zero-filled 
array and returns the final modified array.

Each update operation is represented as a tuple/list of three values: (start_index, end_index, increment_value), where:

start_index: The starting index of the range (inclusive)
end_index: The ending index of the range (inclusive)
increment_value: The value to add to all elements in the range [start_index, end_index]
    
    Args:
        length: The size of the array (initially filled with zeros)
        updates: A list of tuples (start_index, end_index, increment_value)
        
    Returns:
        list: The modified array after applying all updates
"""
import unittest
def apply_range_updates(length: int, updates: list) -> list:

    startarray = [0] * length
    print(startarray)
    modifiedarray = startarray.copy()
    try:
        for indexvals in updates:
            start_index, end_index, increment_value = indexvals[0],indexvals[1],indexvals[2]
            print(start_index, end_index, increment_value)
            
            # for _ in range(start_index, end_index + 1):
            #     modifiedarray[_] += increment_value
            #     print(_, modifiedarray)

            modifiedarray[start_index: end_index + 1] = [x + increment_value for x in modifiedarray[start_index: end_index + 1] ]
            print(modifiedarray)
    except Exception as e:
        print(f"Error : {e}")
    return modifiedarray

class TestRangeUpdate(unittest.TestCase):
    def test_range_update(self):
        test_data = [
            # (length, updates, expected_result)
            (5, [(1, 3, 2)], [0, 2, 2, 2, 0]),
            (5, [(1, 3, 2), (2, 4, 3)], [0, 2, 5, 5, 3]),
            (10, [(2, 4, 5), (3, 6, -2), (1, 5, 3)], [0, 3, 8, 6, 6, 1, -2, 0, 0, 0]),
            (3, [], [0, 0, 0]),
            (6, [(0, 5, 1), (0, 2, 2), (3, 5, -1)], [3, 3, 3, 0, 0, 0]),
            (8, [(0, 7, 1)], [1, 1, 1, 1, 1, 1, 1, 1]),
            (7, [(2, 5, 3), (0, 3, -1), (4, 6, 2)], [-1, -1, 2, 2, 5, 5, 2]),
            (4, [(0, 0, 5), (3, 3, 10)], [5, 0, 0, 10]),
            (5, [(0, 4, 2), (1, 3, -1), (2, 2, 3)], [2, 1, 4, 1, 2]),
            (1, [(0, 0, 100)], [100]),
            (6, [(1, 4, 5), (2, 3, -3), (0, 1, 2), (4, 5, 1)], [2, 7, 2, 2, 6, 1]),
            (10, [(0, 9, 1), (5, 9, -1), (0, 4, 1)], [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]),
            (5, [(0, 4, 10), (0, 4, -10)], [0, 0, 0, 0, 0]),
            (8, [(1, 6, 4), (3, 5, 2), (0, 2, -1), (5, 7, 3)], [-1, 3, 3, 6, 6, 9, 7, 3]),
            (3, [(0, 2, 1), (0, 2, 1), (0, 2, 1)], [3, 3, 3])
        ]
    
        for length, updates, expected in test_data:
            with self.subTest(length=length, updates=updates, expected=expected):
                self.assertEqual(apply_range_updates(length=length, updates=updates), expected)

if __name__ == "__main__":
    unittest.main()
    #apply_range_updates(length=5, updates= [(1, 3, 2), (2, 4, 3)])
