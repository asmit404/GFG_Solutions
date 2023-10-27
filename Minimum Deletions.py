"""
Title     : Minimum Deletions
Author    : Asmit Singh
Solved On   : 27 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def minimumNumberOfDeletions(self, S):
        n = len(S)
        dp = [0] * (n+1)
        rev = S[::-1]
        for i in range(1, n+1):
            prev = 0
            for j in range(1, n+1):
                temp = dp[j]
                if S[i-1] == rev[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        return n - dp[n]

# Time Complexity: O(n^2)
# Space Complexity: O(n)