'''
Title     : Row with minimum number of 1s
Author    : Asmit Singh
Solved On   : 22 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def minRow(self, n, m, a):
        res = None
        minCount = float("inf")
        for row in range(n):
            count = a[row].count(1)
            if count < minCount:
                minCount = count
                res = row+1
            if minCount == 0: break
        return res

# Time Complexity: O(n * m)
# Space Complexity: O(1)