'''
Title     : Arithmetic Number
Domain    : Mathematical, Algorithms
Author    : Asmit Singh
Solved On   : 13 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def inSequence(self, A, B, C):
        if ((C != 0 and (B-A)%C == 0) or C == 0) and ((C > 0 and B >= A) or (C < 0 and B <= A) or (C == 0 and B == A)):
            return 1
        else:
            return 0
