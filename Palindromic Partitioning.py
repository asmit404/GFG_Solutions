"""
Title     : Palindromic Partitioning
Author    : Asmit Singh
Solved On   : 24 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        min_cost = [0] * (n+1)
        for i in range(n+1):
            min_cost[i] = i-1
        for i in range(1, n+1):
            for j in range(i):
                substring = string[j:i]
                if substring == substring[::-1]:
                    min_cost[i] = min(min_cost[i], min_cost[j]+1)
        return min_cost[n]

# The most braindead solution I could think of.
# Time Complexity: O(N^2)
# Space Complexity: O(N)