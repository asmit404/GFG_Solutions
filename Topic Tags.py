'''
Title     : Topic Tags
Domain    : Arrays, Sorting, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 24 Jan 2023
Solved Using   : Python3
'''

class Solution:
    def convert(self,arr, n):
        ans = []
        sorted_arr = sorted(arr)
        index_map = {val: i for i, val in enumerate(sorted_arr)}
        for i, val in enumerate(arr):
            arr[i] = index_map[val]
