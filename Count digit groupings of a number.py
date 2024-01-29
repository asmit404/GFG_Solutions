"""
Title     : Count digit groupings of a number
Author    : Asmit Singh
Solved On   : 29 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def solve(self, cp, cs, sz, s, dp):
        if cp == sz: return 1
        if dp[cp][cs] != -1: return dp[cp][cs]
        sm, cnt = 0, 0

        for i in range(cp, sz):
            sm += int(s[i])
            if sm >= cs:
                cnt += self.solve(i + 1, sm, sz, s, dp)

        dp[cp][cs] = cnt
        return cnt

    def TotalCount(self, s):
        sm = sum(map(int, s))
        dp = [[-1] * (sm + 1) for _ in range(len(s) + 1)]
        return self.solve(0, 0, len(s), s, dp)

# Time Complexity: O(n ^ 2 * sum)
# Space Complexity: O(n * sum)