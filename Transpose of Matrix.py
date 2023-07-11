'''
Title     : Smallest Positive missing number
Author    : Asmit Singh
Solved On   : 10 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def transpose(self, matrix, n):
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
