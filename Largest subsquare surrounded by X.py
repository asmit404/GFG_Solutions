'''
Title     : Largest subsquare surrounded by X
Author    : Asmit Singh
Solved On   : 14 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def largestSubsquare(self, n, a):
        res = 0
        hor = [[0]*n for _ in range(n)]
        ver = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    hor[i][j] = 1 if j == 0 else hor[i][j-1] + 1
                    ver[i][j] = 1 if i == 0 else ver[i-1][j] + 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                size = min(ver[i][j], hor[i][j])
                while size > res:
                    if (ver[i][j - size + 1] >= size) and (hor[i - size + 1][j] >= size):
                        res = size
                    size -= 1
        return res

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n ^ 2)