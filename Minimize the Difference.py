'''
Title     : Minimize the Difference
Author    : Asmit Singh
Solved On   : 16 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def minimizeDifference(self, n, k, arr):
        p_max = [0] * n
        p_min = [0] * n
        p_max[n - 1] = p_min[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            p_max[i] = max(arr[i], p_max[i + 1])
            p_min[i] = min(arr[i], p_min[i + 1])

        mini, maxi = arr[0], arr[0]
        res = p_max[k] - p_min[k]

        for i in range(1, n - k):
            res = min(res, max(maxi, p_max[i + k]) - min(mini, p_min[i + k]))
            mini = min(mini, arr[i])
            maxi = max(maxi, arr[i])
        res = min(res, maxi - mini)

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)