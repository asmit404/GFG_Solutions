'''
Title     : Xoring and Clearing
Author    : Asmit Singh
Solved On   : 14 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def printArr(self, n, arr):
        print(' '.join(map(str, arr)))

    def setToZero(self, n, arr):
        for i in range(len(arr)):
            arr[i] = 0

    def xor1ToN(self, n, arr):
        for i in range(len(arr)):
            arr[i] ^= i

# Time Complexity: O(n)
# Space Complexity: O(n)