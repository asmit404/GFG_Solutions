'''
Title     : Shortest XY distance in Grid
Domain    : Dynamic Programming, BFS, Data Structures
Author    : Asmit Singh
Solved On   : 20 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def shortestXYDist(self, G, N, M):
        i = 10**8
        dp = [[i] * (M+2) for _ in range(N+2)]
        for r in range(1, N+1):
            for c in range(1, M+1):
                dp[r][c] = 0 if G[r-1][c -1] == 'X' else min(dp[r-1][c], dp[r][c-1])+1
        for r in range(N, 0, -1):
            for c in range(M, 0, -1):
                dp[r][c] = min(dp[r][c], 1+dp[r+1][c], 1+dp[r][c+1])
        ans = min(dp[r][c] for r in range(1, N+1)
                  for c in range(1, M+1) if G[r-1][c-1] == 'Y')
        return ans
