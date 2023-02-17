'''
Title     : Is it Fibonacci
Domain    : Arrays, Data Structures, Sliding-Window
Author    : Asmit Singh
Solved On   : 17 Feb 2023
Solved Using   : Python3
'''

class Solution():
    def solve(self, N, K, GeekNum):
        step=K
        while K<N:
            GeekNum.append(sum(GeekNum[-1:-(step+1):-1]))
            K+=1
        return GeekNum[-1]
