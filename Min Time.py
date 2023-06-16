'''
Title     : Min Time
Author    : Asmit Singh
Solved On   : 16 Jun 2023
Solved Using   : Python3
'''

from collections import defaultdict
class Solution:
    def minTime(self, n, locations, types):
        dic = defaultdict(list)
        var = set()
        for a, b in zip(locations, types):
            dic[b].append(a)
            var.add(b)
        var.add(10**10)
        dic[10**10] = [0]
        var = list(sorted(var))
        dp = [[0]*2 for _ in range(len(var)+1)]
        for el in dic.keys():
            dic[el].sort()
        p_left, p_right = 0, 0
        for i, c in enumerate(var):
            left, right = dic[c][0], dic[c][-1]
            dp[i+1][0] = abs(right-left)+min(dp[i][0] + abs(right-p_left), dp[i][1]+abs(p_right-right))
            dp[i+1][1] = abs(right-left)+min(dp[i][0] + abs(left-p_left), dp[i][1]+abs(left-p_right))
            p_left, p_right = left, right
        return (min(dp[-1]))
