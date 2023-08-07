"""
Title     : Solve the Sudoku
Author    : Asmit Singh
Solved On   : 07 Aug 2023
Solved Using   : Python3
"""

class Solution:

    def SolveSudoku(self, grid):
        def isValid(num, grid, row, col):
            for i in range(9):
                if (grid[row][i] == num):
                    return False

            for i in range(9):
                if (grid[i][col] == num):
                    return False

            rr = row-row % 3
            cc = col-col % 3

            for i in range(3):
                for j in range(3):
                    if (grid[rr+i][cc+j] == num):
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if (grid[i][j] == 0):
                    for k in range(1, 10):
                        if (isValid(k, grid, i, j)):
                            grid[i][j] = k
                            ans = self.SolveSudoku(grid)
                            if (ans):
                                return True
                            else:
                                grid[i][j] = 0
                    return False
        return True

    def printGrid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")

# Time Complexity : O(9^(n*n))
# Space Complexity : O(n*n)
