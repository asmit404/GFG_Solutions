'''
Title     : Sum of Products
Author    : Asmit Singh
Solved On   : 12 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def pairAndSum(self, n, arr):
        res = 0
        for pos in range(32):
            cnt = 0
            for num in arr:
                if (num >> pos) & 1:
                    cnt += 1
            if cnt > 1:
                res += (2**pos)*((cnt-1) * cnt)//2
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)