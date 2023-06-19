'''
Title     : Rearrange an array with O(1) extra space
Author    : Asmit Singh
Solved On   : 19 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def arrange(self, arr, n):
        for i in range(n):
            arr[i] = (arr[arr[i]] % n)*n+arr[i]
        for j in range(n):
            arr[j] //= n
