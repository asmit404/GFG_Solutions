'''
Title     : Max Sum without Adjacents
Domain    : Arrays, Dynamic Programming, Data Structures, Algorithms 
Author    : Asmit Singh
Solved On   : 04 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def findMaxSum(self,arr, n):
        if n==1: return arr[0]
        if n==2: return max(arr[0], arr[1])

        dp = [-1 for i in range(n)]
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])
        for i in range(2, n): dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        return dp[-1]
