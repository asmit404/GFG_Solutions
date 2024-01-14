"""
Title     : Find duplicate rows in a binary matrix
Author    : Asmit Singh
Solved On   : 14 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def repeatedRows(self, arr, m, n):
        res = []
        s = set()
        for i in range(len(arr)):
            row_str = ''.join(map(str, arr[i]))
            if row_str not in s:
                s.add(row_str)
            else:
                res.append(i)
        return res

# Time Complexity : O(m * n)
# Space Complexity : O(m * n)