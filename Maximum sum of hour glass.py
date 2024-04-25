'''
Title     : Maximum sum of hour glass
Author    : Asmit Singh
Solved On   : 25 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def findMaxSum(self, n, m, mat):
        if n < 3 or m < 3: return -1
        res = float('-inf')
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                curr = mat[i][j]
                curr += mat[i - 1][j] + mat[i - 1][j - 1] + mat[i - 1][j + 1]
                curr += mat[i + 1][j] + mat[i + 1][j - 1] + mat[i + 1][j + 1]
                res = max(res, curr)
        return res

# Time Complexity: O(n * m)
# Space Complexity: O(1)