'''
Title     : Gray to Binary equivalent
Author    : Asmit Singh
Solved On   : 11 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def grayToBinary(self, n):
        binary = format(n, 'b')
        res = binary[0]
        for i in range(1, len(binary)):
            res += str(int(res[-1]) ^ int(binary[i]))
        return int(res, 2)

# Time Complexity: O(n)
# Space Complexity: O(n)