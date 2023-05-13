'''
Title     : Bit Operations
Author    : Asmit Singh
Solved On   : 13 May 2023
Solved Using   : Python3
'''

class Solution:
    def bitMagic(self, n, arr):
        c = 0
        for i in range(n):
            if arr[i] != arr[n-i-1]:
                c += 1
        x = c//2
        return (x+1)//2
