'''
Title     : Minimum Days
Domain    : Strings, Permutations, Data Structures
Author    : Asmit Singh
Solved On   : 11 Feb 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        dic={d:i+1 for i,d in enumerate(P)}
        result=0
        for i in range(N-1):
            if S[i]==S[i+1]:
                x=dic[i]
                y=dic[i+1]
                result=max(result,min(x,y))
        return result
