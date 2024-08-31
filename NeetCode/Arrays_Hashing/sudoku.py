'''You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
'''
import unittest
from collections import defaultdict

def sudoko_mine(incoming: list[list[str]]) -> bool:
    # print(f"Incoming is {incoming}")
    l_row = len(incoming)
    l_col = len(incoming[0])
    valid_values = [str(x) for x in range(1,10)]
    valid_values.append(".")
    print(valid_values)
    if (l_col != l_row) and (l_row !=9):
        # print(f"False in One")
        return False
    for row in range(l_row):
        seen = []
        for col in range(l_col):
            # print(f"ROW is {row} and col is {col}")
            # print(f"INCOMING[row][col] is {incoming[row][col]}")
            try:
                if (incoming[row][col]) not in valid_values or (incoming[row][col]) in seen:
                    # print(f"False in TWO")
                    return False
                if incoming[row][col] != ".":
                    seen.append(incoming[row][col])                

            except: # if not an integer in str format
                # print(f"False in THREE")
                return False
    er = ec = 3
    sr = sc = 0
    seen = []
    tracker = 0
    for row in range(sr, er + 1):   
        print(f" ec : {ec} er : {er} and row {row}")           
        for col in range(sc, ec):
            # print(f"ROW AGAIN is {row} and col AGAIN is {col}")
            print(f"INCOMING{[row]}{[col]} AGAIN is {incoming[row][col]}") 
            print(f"Seen is {seen}")        
            if incoming[row][col] in seen:
                print(f"False in TWO AGAIN")
                return False
            if incoming[row][col] != ".":
                seen.append(incoming[row][col])   
            tracker += 1
            print(f"Tracker is {tracker}")
            if tracker % 9 == 0:            
                seen = []         
                ec += 3
                sc += 3   
                row = 0   
            print(f" ec : {ec} er : {er} and row {row}")      
    return True

def isValidSudoku(incoming: list[list[str]]) -> bool:
        board = incoming
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

class TestSudoko(unittest.TestCase):
    def test_sudoko(self):
        test_data = [
            {'input': [["1","2",".",".","3",".",".",".","."],
                        ["4",".",".","5",".",".",".",".","."],
                        [".","9","8",".",".",".",".",".","3"],
                        ["5",".",".",".","6",".",".",".","4"],
                        [".",".",".","8",".","3",".",".","5"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".",".",".",".",".",".","2",".","."],
                        [".",".",".","4","1","9",".",".","8"],
                        [".",".",".",".","8",".",".","7","9"]], 'expected': True},
            {'input': [["1","2",".",".","3",".",".",".","."],
                        ["4",".",".","5",".",".",".",".","."],
                        [".","9","1",".",".",".",".",".","3"],
                        ["5",".",".",".","6",".",".",".","4"],
                        [".",".",".","8",".","3",".",".","5"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".",".",".",".",".",".","2",".","."],
                        [".",".",".","4","1","9",".",".","8"],
                        [".",".",".",".","8",".",".","7","9"]], 'expected': False},    
        ] 
        for test_case in test_data:
            with self.subTest(test_case=test_case):
                # print(f"Sending from HERE : {test_case['input']}")
                actual = isValidSudoku(incoming=test_case['input'])
                expected = test_case['expected']
                self.assertEqual(actual, expected, f"Failed for {test_case}. Received {actual}")

if __name__ == "__main__":
    unittest.main()
         