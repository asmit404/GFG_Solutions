"""
Title     : Boolean Matrix
Author    : Asmit Singh
Solved On   : 30 Sept 2023
Solved Using   : Python3
"""

def booleanMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_flags = [False] * rows
    col_flags = [False] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_flags[i] = True
                col_flags[j] = True

    for i in range(rows):
        for j in range(cols):
            if row_flags[i] or col_flags[j]:
                matrix[i][j] = 1

# Time Complexity: O(n*m)
# Space Complexity: O(n+m)