"""
Title     : Brother From Different Roots
Author    : Asmit Singh
Solved On   : 03 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def inOrder(self, root):
        if root:
            yield from self.inOrder(root.left)
            yield root.data
            yield from self.inOrder(root.right)

    def countPairs(self, root1, root2, x):
        r1, r2 = self.inOrder(root1), reversed(list(self.inOrder(root2)))
        val1, val2 = next(r1, None), next(r2, None)
        res = 0
        while val1 is not None and val2 is not None:
            if val1 + val2 == x:
                res += 1
                val1, val2 = next(r1, None), next(r2, None)
            elif val1 + val2 < x:
                val1 = next(r1, None)
            else:
                val2 = next(r2, None)
        return res

# Time Complexity  : O(n + m)
# Space Complexity : O(n + m)