"""
Title     : Wave Array
Author    : Asmit Singh
Solved On   : 28 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def convertToWave(self ,n, a):
        for i in range(0, n-1, 2):
            a[i], a[i+1] = a[i+1], a[i]

# Time Complexity: O(n)
# Space Complexity: O(1)