"""
Title     : Making A Large Island
Author    : Asmit Singh
Solved On   : 16 Oct 2023
Solved Using   : Python3
"""

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def get_id(row, col): return row * cols + col

        island_ids = [0] * (rows * cols)
        island_sizes = [1] * (rows * cols)
        for row in range(rows):
            for col in range(cols):
                island_id = get_id(row, col)
                island_ids[island_id] = island_id

        visited = set()

        def dfs(row, col, root):
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == 0 or (row, col) in visited:
                return
            visited.add((row, col))
            current_id = get_id(row, col)
            if current_id != root:
                island_sizes[root] += 1
                island_sizes[current_id] = 0
                island_ids[current_id] = root

            dfs(row+1, col, root)
            dfs(row-1, col, root)
            dfs(row, col-1, root)
            dfs(row, col+1, root)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col, get_id(row, col))

        max_island_size = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    current_size = 1
                    connected_islands = set()
                    for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                            rc_id = get_id(r, c)
                            root = island_ids[rc_id]
                            if root not in connected_islands:
                                connected_islands.add(root)
                                current_size += island_sizes[root]
                    max_island_size = max(max_island_size, current_size)
        return rows * cols if max_island_size == 0 else max_island_size

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)