"""
Title     : Shortest Source to Destination Path
Author    : Asmit Singh
Solved On   : 02 Aug 2023
Solved Using   : Python3
"""

from collections import deque
class Solution:
    def shortestDistance(self, num_rows, num_cols, grid, dest_row, dest_col):
        queue, visited = deque([(0, 0, 0)]), {(0, 0)}
        while queue:
            row, col, steps = queue.popleft()
            if row == dest_row and col == dest_col:
                return steps
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + row_offset, col + col_offset
                if (
                    0 <= next_row < num_rows
                    and 0 <= next_col < num_cols
                    and grid[next_row][next_col]
                    and (next_row, next_col) not in visited
                ):
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        return -1

# Time Complexity  : O(m * n)
# Space Complexity : O(m * n)