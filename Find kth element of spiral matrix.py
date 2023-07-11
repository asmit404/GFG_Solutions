'''
Title     : Find kth element of spiral matrix
Author    : Asmit Singh
Solved On   : 11 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def findK(self, a, n, m, k):
        cnt, rows, cols, cntk = 0, 0, 0, 0
        rowe, cole = n-1, m-1

        while cnt < n*m:
            for i in range(cols, cole+1):
                cntk += 1
                cnt += 1
                if cntk == k:
                    return a[rows][i]
            rows += 1

            for i in range(rows, rowe+1):
                cntk += 1
                cnt += 1
                if cntk == k:
                    return a[i][cole]
            cole -= 1

            for i in range(cole, cols-1, -1):
                cntk += 1
                cnt += 1
                if cntk == k:
                    return a[rowe][i]
            rowe -= 1

            for i in range(rowe, rows-1, -1):
                cntk += 1
                cnt += 1
                if cntk == k:
                    return a[i][cols]
            cols += 1
