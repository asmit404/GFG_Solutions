'''
Title     : K Largest Elements
Author    : Asmit Singh
Solved On   : 13 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def kLargest(self, arr, n, k):
        arr.sort(reverse=True)
        return arr[:k]
