"""
Title     : Longest Repeating Subsequence
Author    : Asmit Singh
Solved On   : 18 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def LongestRepeatingSubsequence(self, str):
        n = len(str)
        d = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        return d[n][n]
