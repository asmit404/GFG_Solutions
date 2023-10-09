"""
Title     : Height of Binary Tree
Author    : Asmit Singh
Solved On   : 9 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def height(self, root):
        if not root: return 0
        l, r = self.height(root.left), self.height(root.right)
        return 1 + max(l, r)

# Time Complexity: O(n)
# Space Complexity: O(n)