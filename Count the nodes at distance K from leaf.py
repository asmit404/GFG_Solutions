"""
Title     : Count the nodes at distance K from leaf
Author    : Asmit Singh
Solved On   : 06 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def printKDistantfromLeaf(self, root, k):
        pool, res = [], set()
        def compute(root, path, dist):
            if root is None: return
            path.append(root)
            if root.left is None and root.right is None and dist >= k:
                res.add(path[dist - k])
            else:
                compute(root.left, path, dist + 1)
                compute(root.right, path, dist + 1)
            path.pop()
        compute(root, pool, 0)
        return len(res)

# Time Complexity: O(n)
# Space Complexity: O(n)