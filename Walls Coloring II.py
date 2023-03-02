'''
Title     : Walls Coloring II
Domain    : Dynamic Programming
Author    : Asmit Singh
Solved On   : 2 Mar 2023
Solved Using   : Python3
'''

import numpy as np
class Solution:
    def minCost(self, costs):
        N, K = len(costs), len(costs[0])
        if N <= 0 or K <= 0 or (K == 1 and N >= 2):
            return -1
        dp, tmp = costs[0].copy(), [0]*K
        for i in range(1, N):
            min1 = np.argmin(dp)
            min2 = min((v, i) for i, v in enumerate(dp) if i != min1)[1]
            for j in range(K):
                tmp[j] = costs[i][j] + (dp[min1] if min1 != j else dp[min2])
            dp, tmp = tmp, dp
        return min(dp)
