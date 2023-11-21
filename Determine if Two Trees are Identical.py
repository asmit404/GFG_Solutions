"""
Title     : Determine if Two Trees are Identical
Author    : Asmit Singh
Solved On   : 21 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def isIdentical(self, root1, root2):
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.data != root2.data:
                return False
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        return dfs(root1, root2)

# Time Complexity : O(n)
# Space Complexity : O(h)