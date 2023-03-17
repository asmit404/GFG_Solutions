'''
Title     : Number of Subarrays of 0s
Domain    : Arrays, Mathematical
Author    : Asmit Singh
Solved On   : 17 Mar 2023
Solved Using   : Python3
'''

class Solution():
    def no_of_subarrays(self, n, arr):
        count = 0
        ans = 0
        for v in arr:
            if v == 0:
                count += 1
                ans += count
            else:
                count = 0
        return ans
