"""
Title     : Largest Sum Subarray of Size at least K
Author    : Asmit Singh
Solved On   : 2 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def maxSumWithK(self, a, n, k):
        max_sum = [a[0]] + [0] * (n - 1)
        for i in range(1, n):
            max_sum[i] = max(a[i], max_sum[i - 1] + a[i])
        var = ans = sum(a[:k])
        for i in range(k, n):
            var = var + a[i] - a[i - k]
            ans = max(ans, var, var + max_sum[i - k])
        return ans

# Time Complexity  : O(n)
# Space Complexity : O(n)