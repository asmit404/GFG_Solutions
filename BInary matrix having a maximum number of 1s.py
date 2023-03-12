'''
Title     : Binary matrix having maximum number of 1s
Domain    : Binary Search, Algorithms
Author    : Asmit Singh
Solved On   : 12 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def findMaxRow(self, mat, N):
        ans = [0, 0]
        for i in range(N):
            j = N-1-ans[-1]
            while (mat[i][j] == 1 and j >= 0):
                ans[0] = i
                j -= 1
            ans[-1] = N-1-j
        return ans
