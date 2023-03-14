'''
Title     : Maximum Number of Coins
Domain    : Dynamic Programming, Matrix, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 14 Mar 2023
Solved Using   : Python3
'''

class Solution():
    def maxCoins(self, N, a):
        A = a
        A = [1] + A + [1]
        memo = [[None]*(N+2) for i in range(N+2)]

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            if i > j:
                return 0
            if i == j:
                return A[i-1]*A[i]*A[i+1]
            ans = 0
            for k in range(i, j+1):
                ans = max(ans, dp(i, k-1) + dp(k+1, j) + A[i-1]*A[k]*A[j+1])
            memo[i][j] = ans
            return ans
        return dp(1, N)
