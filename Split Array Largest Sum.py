"""
Title     : Split Array Largest Sum
Author    : Asmit Singh
Solved On   : 7 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def isPossible(self, arr, N, K, mid):
        count = curr = 0
        for i in range(N):
            curr += arr[i]
            if curr > mid:
                count += 1
                curr = arr[i]
        count += 1
        return count <= K

    def splitArray(self, arr, N, K):
        low, high = max(arr), sum(arr)
        while low < high:
            mid = (low + high) // 2
            if self.isPossible(arr, N, K, mid):
                high = mid
            else:
                low = mid + 1
        return low

# Time Complexity : O(N log(sum(arr)))
# Space Complexity : O(1)