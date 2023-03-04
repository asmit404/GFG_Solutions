'''
Title     : Best Node
Domain    : Tree, DFS
Author    : Asmit Singh
Solved On   : 4 Mar 2023
Solved Using   : Python3
'''

from typing import List
neg = -10**11
class Solution:
    def bestNode(self, N: int, A: List[int], P: List[int]) -> int:
        leaves = set([i for i in range(1, N+1)])
        ans = [neg for i in range(N+1)]
        for i in P:
            if i in leaves:
                leaves.remove(i)
        for i in leaves:
            pointer = i
            lmao = 0
            while pointer != -1:
                lmao = A[pointer-1] - lmao
                ans[pointer] = max(lmao, ans[pointer])
                pointer = P[pointer-1]
        return max(ans)

# Don't ask me how it works, I don't know either.