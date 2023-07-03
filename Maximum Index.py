'''
Title     : Maximum Index
Author    : Asmit Singh
Solved On   : 3 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def maxIndexDiff(self, arr, n):
        v_min = [0] * n
        v_max = [0] * n
        v_min[0] = arr[0]
        v_max[n - 1] = arr[n - 1]
        for i in range(1, n):
            v_min[i] = min(v_min[i - 1], arr[i])
            v_max[n - i - 1] = max(v_max[n - i], arr[n - i - 1])
        res = 0
        var1 = 0
        var2 = 0
        while var1 < n and var2 < n:
            if v_min[var1] <= v_max[var2]:
                res = max(res, var2 - var1)
                var2 += 1
            else:
                var1 += 1
        return res
