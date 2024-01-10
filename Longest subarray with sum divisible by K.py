"""
Title     : Longest subarray with sum divisible by K
Author    : Asmit Singh
Solved On   : 10 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def longSubarrWthSumDivByK(self, arr, n, k):
        res = rem = 0
        hmap = {0: -1}
        for i in range(n):
            rem = (rem + arr[i]) % k
            if rem in hmap:
                res = max(res, i - hmap[rem])
            else:
                hmap[rem] = i
        return res

# Time Complexity : O(n)
# Space Complexity : O(k)