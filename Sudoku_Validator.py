''''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''
class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        for i in range(9):
            if not self.validList([grid[i][j] for j in range(0,9)]):
                return False
        for j in range(9):
            if not self.validList([grid[i][j] for i in range(0,9)]):
                return False

        for i in range(3):
            for j in range(3):
                if not self.validList([grid[x][y] for x in range(i*3,3*i+3) for y in range(3*j,3*j+3) ] ):
                    return False
        return True
    def validList(self,x: List)-> bool:
            xs = filter(lambda y: y != ".", x)
            xs= [i for i in xs]
            return True if len(xs)==len(set(xs)) else False
