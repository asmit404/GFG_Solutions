"""
Title     : Array Pair Sum Divisibility Problem
Author    : Asmit Singh
Solved On   : 1 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def canPair(self, nums, k):
        if len(nums) % 2 != 0: return False
        cnt = [0] * k
        for num in nums:
            cnt[num % k] += 1
        for i in range(1, k // 2 + 1):
            if cnt[i] != cnt[k - i]:
                return False
        return True

# Time Complexity  : O(n + k)
# Space Complexity : O(k)