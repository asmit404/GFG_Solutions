'''
Title     : Merge Without Extra Space
Author    : Asmit Singh
Solved On   : 7 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def merge(self, arr1, arr2, n, m):
        arr1 += arr2
        arr1.sort()
        arr2.clear()
        arr2 = arr1[n:]
        arr1 = arr1[:n]
        return (arr1, arr2)
