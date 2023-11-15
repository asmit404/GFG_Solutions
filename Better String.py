"""
Title     : Better String
Author    : Asmit Singh
Solved On   : 15 Nov 2023
Solved Using   : Python3
"""

def countSub(ss):
    last = [-1 for _ in range(257)]
    n = len(ss)
    dp = [-2 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        if last[ord(ss[i - 1])] != -1:
            dp[i] = dp[i] - dp[last[ord(ss[i - 1])]]
        last[ord(ss[i - 1])] = i - 1
    return dp[n]

class Solution:
    def betterString(self, str1, str2):
        if countSub(str1) >= countSub(str2):
            return (str1)
        else:
            return (str2)

# Time Complexity: O(n)
# Space Complexity: O(n)