"""
Title     : Largest rectangular sub-matrix whose sum is 0
Author    : Asmit Singh
Solved On   : 26 Dec 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def sumZeroMatrix(self, a: List[List[int]]) -> List[List[int]]:
        m, n = len(a), len(a[0])
        left = right = up = down = 0

        for i in range(n):
            arr = [0] * m
            for j in range(i, n):
                for k in range(m):
                    arr[k] += a[k][j]
                sum_map = {0: -1}
                l = r = curr_sum = 0

                for k in range(m):
                    curr_sum += arr[k]
                    if curr_sum in sum_map:
                        new_l, new_r = sum_map[curr_sum] + 1, k + 1
                        if new_r - new_l > r - l:
                            l, r = new_l, new_r
                    else:
                        sum_map[curr_sum] = k

                if (j - i + 1) * (r - l) > (right - left) * (down - up):
                    up, down, left, right = l, r, i, j + 1

        return [[a[i][j] for j in range(left, right)] for i in range(up, down)]

# Time Complexity  : O(n ^ 3 * r)?
# Space Complexity : O(r)?