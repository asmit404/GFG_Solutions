'''
Title     : Print N-bit binary numbers having more 1s than 0s
Author    : Asmit Singh
Solved On   : 25 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def NBitBinary(self, n, string = '1', length = 1, zeros = 0):
        if length == n: return [string]
        return self.NBitBinary(n, string + '1', length + 1, zeros) + (self.NBitBinary(n, string + '0', length + 1, zeros+1) if (length - zeros) > zeros else [])

# Time Complexity: O(2 ^ n)
# Space Complexity: O(n)