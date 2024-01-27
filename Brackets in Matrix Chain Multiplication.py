"""
Title     : Brackets in Matrix Chain Multiplication
Author    : Asmit Singh
Solved On   : 27 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def matrixChainOrder(self, p, n):
        inf = float('inf')
        cost = [[inf]*n for _ in range(n)]
        res = [['']*n for _ in range(n)]

        for i in range(n - 1):
            cost[i][i + 1] = 0
            res[i][i + 1] = chr(ord('A') + i)

        for i in range(2, n):
            for j in range(n - i):
                x = i + j
                for k in range(j + 1, n):
                    temp = cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]
                    if cost[j][x] > temp:
                        cost[j][x] = temp
                        res[j][x] = '({}{})'.format(res[j][k], res[k][x])

        return res[0][n - 1]

# Time Complexity: O(n ^ 3)
# Space Complexity: O(n ^ 2)