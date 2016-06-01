import string
import numpy
from math import sqrt


class Sudoku(object):

    def __init__(self, board):
        self.board = board
        self.rows = self.board
        self.cols = zip(*self.rows)
        self.rowsN = len(board)
        self.colsN = len(board[0])
        self.boardsqrt = int(sqrt(self.colsN))

    def is_valid(self):
        valid_set = set(map(int, string.digits[1:self.colsN+1]))

        # Validate square root of N is an integer
        if not self.boardsqrt == sqrt(self.colsN):
            return False

        # Validate array is N x N
        if not all(map(lambda row: len(row) == self.colsN, self.rows)):
            return False
        
        # Validate all rows and columns contain integers 1 through N
        if not all(map(lambda row: set(row) == valid_set, self.rows)):
            return False
        if not all(map(lambda col: set(col) == valid_set, self.cols)):
            return False

        # Validate all sum-matrices contain integers 1 through N
        for i in range(0, self.rowsN, self.boardsqrt):
            for j in range(0, self.colsN, self.boardsqrt):
                print self.board[i:i+self.boardsqrt, j:j+self.boardsqrt]
        
        return True


# Test Cases

# Valid Sudoku

goodSudoku1 = Sudoku([
  [7, 8, 4,  1, 5, 9,  3, 2, 6],
  [5, 3, 9,  6, 7, 2,  8, 4, 1],
  [6, 1, 2,  4, 3, 8,  7, 5, 9],

  [9, 2, 8,  7, 1, 5,  4, 6, 3],
  [3, 5, 7,  8, 4, 6,  1, 9, 2],
  [4, 6, 1,  9, 2, 3,  5, 8, 7],

  [8, 7, 6,  3, 9, 4,  2, 1, 5],
  [2, 4, 3,  5, 6, 1,  9, 7, 8],
  [1, 9, 5,  2, 8, 7,  6, 3, 4]
])

goodSudoku2 = Sudoku([
  [1, 4,  2, 3],
  [3, 2,  4, 1],

  [4, 1,  3, 2],
  [2, 3,  1, 4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9],

  [1, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9],

  [1, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9],
  [1, 2, 3,  4, 5, 6,  7, 8, 9]
])

badSudoku2 = Sudoku([
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4],
  [1, 2, 3, 4],
  [1]
])

print goodSudoku1.is_valid(), True, 'Testing valid 9x9'
print goodSudoku2.is_valid(), True, 'Testing valid 4x4'

print badSudoku1.is_valid(), False, 'Values in wrong order'
print badSudoku2.is_valid(), False, '4x5 (invalid dimension)'
