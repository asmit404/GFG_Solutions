'''
Title     : Minimum Points To Reach Destination
Author    : Asmit Singh
Solved On   : 9 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def minPoints(self, m, n, points):
        pool = [[0 for _ in range(n)] for _ in range(m)]
        pool[m-1][n-1] = max(1, 1 - points[m-1][n-1])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue

                if i == m-1:
                    pool[i][j] = max(1, pool[i][j+1] - points[i][j])
                elif j == n-1:
                    pool[i][j] = max(1, pool[i+1][j] - points[i][j])
                else:
                    pool[i][j] = max(
                        1, min(pool[i+1][j], pool[i][j+1]) - points[i][j])

        return pool[0][0]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)