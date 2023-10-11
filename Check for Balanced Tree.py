"""
Title     : Check for Balanced Tree
Author    : Asmit Singh
Solved On   : 11 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return height(root) != -1

# Time Complexity: O(n)
# Space Complexity: O(n)