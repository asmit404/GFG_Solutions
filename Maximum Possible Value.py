'''
Title     : Maximum Possible Value
Domain    : Mathematical, Algorithms
Author    : Asmit Singh
Solved On   : 13 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def maxPossibleValue(self, N, A, B):
        ts = 0
        ans = 0
        m = 1000000007
        for i in range(N):
            if B[i]//2 > 0:
                ans += 2*(B[i]//2)*A[i]
                ts += B[i]//2
                m = min(m, A[i])
        if ts % 2 != 0:
            ans -= 2*m
        return ans
