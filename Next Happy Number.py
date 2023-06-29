'''
Title     : Next Happy Number
Author    : Asmit Singh
Solved On   : 29 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def solve(self, N):
        if (N == 2) or (N == 3) or (N == 4) or (N == 5) or (N == 6) or (N == 8) or (N == 9):
            return False
        if (N == 1 or N == 7):
            return True
        sq_sum = 0
        while (N > 0):
            x = N % 10
            sq_sum += (x * x)
            N = N//10
        return self.solve(sq_sum)

    def nextHappy(self, N):
        # code here
        N += 1
        while (True):
            if self.solve(N):
                return N
            N += 1
