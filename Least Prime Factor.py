'''
Title     : Least Prime Factor
Author    : Asmit Singh
Solved On   : 07 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def leastPrimeFactor(self, n):
        least = [0]*(n+1)
        least[1] = 1
        for i in range(2, n+1):
            for j in range(i, n+1, i):
                if least[j] == 0:
                    least[j] = i
        return least
