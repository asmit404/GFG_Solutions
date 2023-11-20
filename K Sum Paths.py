"""
Title     : K Sum Paths
Author    : Asmit Singh
Solved On   : 20 Nov 2023
Solved Using   : Python3
"""

from collections import defaultdict

class Solution:
    def sumK(self, root, k):
        MOD = 1000000007
        pfs = defaultdict(int)
        pfs[0] = 1
        pool = [0]
        def dfs(node, curr = 0):
            if not node: return
            curr += node.data
            pool[0] += pfs[curr-k]
            pfs[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            pfs[curr] -= 1

        dfs(root)
        return pool[0] % MOD

# Time Complexity : O(n)
# Space Complexity : O(n)