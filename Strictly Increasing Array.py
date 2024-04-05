'''
Title     : Strictly Increasing Array
Author    : Asmit Singh
Solved On   : 5 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def min_operations(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] - nums[j] >= i-j:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_ops = max(dp)
        return n - max_ops

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)