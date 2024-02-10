"""
Title     : Number of paths in a matrix with k coins
Author    : Asmit Singh
Solved On   : 10 Feb 2024
Solved Using   : Python3
"""


class Solution:
    def numberOfPath(self, n, k, arr):
        memo = {}
        def count_paths(row, col, rem):
            if row >= n or col >= n or rem < 0: return 0
            if rem == arr[row][col] and row == n-1 and col == n-1: return 1
            if ((row, col), rem) in memo: return memo[((row, col), rem)]
            memo[((row, col), rem)] = count_paths(row+1, col, rem-arr[row][col]) + count_paths(row, col+1, rem-arr[row][col])
            return memo[((row, col), rem)]
        return count_paths(0, 0, k)

# Time Complexity: O(n ^ 2 * k)
# Space Complexity: O(n ^ 2 * k)