'''
Title     : Scrambled Strings
Domain    : Strings, Recursion, Divide and Conquer, Tree, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 28 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def isScramble(self, S1: str, S2: str) -> bool:
        if len(S1) != len(S2) or sorted(S1) != sorted(S2):
            return False
        n = len(S1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = S1[i] == S2[j]

        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for p in range(1, k):
                        if (dp[i][j][p] and dp[i + p][j + p][k - p]) or (dp[i][j + k - p][p] and dp[i + p][j][k - p]):
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]
