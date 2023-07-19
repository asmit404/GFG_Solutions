"""
Title     : Longest Palindromic Subsequence
Author    : Asmit Singh
Solved On   : 19 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def longestPalinSubseq(self, S):
        n = len(S)
        rev = S[::-1]
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if S[i - 1] == rev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]
