'''
Title     : Adding Ones
Author    : Asmit Singh
Solved On   : 11 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def update(self, a, n, updates, k):
        for i in range(k):
            a[updates[i] - 1] += 1
        for j in range(1, n):
            a[j] += a[j-1]
        return a
