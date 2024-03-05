'''
Title     : Maximum Index
Author    : Asmit Singh
Solved On   : 05 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def maxIndexDiff(self, a, n):
        v_min = [0] * n
        v_max = [0] * n
        v_min[0] = a[0]
        v_max[n - 1] = a[n - 1]
        for i in range(1, n):
            v_min[i] = min(v_min[i - 1], a[i])
            v_max[n - i - 1] = max(v_max[n - i], a[n - i - 1])
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

# Repeated question, also seen on 03 Jul 2023
# Time Complexity: O(n)
# Space Complexity: O(n)