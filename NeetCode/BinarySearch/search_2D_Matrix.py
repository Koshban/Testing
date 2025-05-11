'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
import unittest
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        print(f"Matrix is {matrix}")
        if len(matrix) == 0:
            return False
        lm, rm = 0, len(matrix) -1
        
        while lm <= rm:
            midm = (lm + rm)//2
            if matrix[midm] and matrix[midm][0] > target:
                rm = midm - 1
                print(f"1. rm is {rm} and lm is {lm} and midm is {midm}")
            elif matrix[midm] and matrix[midm][-1] < target:
                lm = midm + 1
                print(f"2")
            else:                
                break

            #midm = (lm + rm)//2
        if not ( lm <= rm):
            print(f"False here 1")
            return False
        finalmatrix = matrix[midm]    
        print(f"Inner List is {finalmatrix}")
        
        l, r = 0, len(finalmatrix) - 1
        
        while l <= r:
            
            m = (l + r)//2
            print(f"4. r is {r} and l is {l} and m is {m} and number is {finalmatrix[m]}")
            if finalmatrix[m] < target:
                l = m + 1
                print(f"1. r is {r} and l is {l} and m is {m} and number is {finalmatrix[m]}")
            elif finalmatrix[m] > target:
                r = m - 1
                print(f"2. r is {r} and l is {l} and m is {m} and number is {finalmatrix[m]}")
            else:
                return True
            print(f"3. r is {r} and l is {l} and m is {m} and number is {finalmatrix[m]}")
            
        print(f"False here 2")
        return False



class TestsearchMatrix(unittest.TestCase):
    def test_searchMatrix(self):
        test_data = [
                {'input': ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), 'expected': True},
                {'input': ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), 'expected': False},
                {'input': ([[1,3,5,7],[10,11,16,20],[23,30,34,60], [63,70,84,90]], 90), 'expected': True},
                {'input': ([], 8), 'expected': False}, 
                {'input': ([[],[]], 8), 'expected': False}, 
            ]
        solution = Solution()
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                #print(f"in Test : Matrix is {test_case['input'][0]}")
                actual = solution.searchMatrix(matrix=test_case['input'][0], target=test_case['input'][1])
                expected = test_case['expected']
                self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()



