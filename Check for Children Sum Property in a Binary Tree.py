"""
Title     : Check for Children Sum Property in a Binary Tree
Author    : Asmit Singh
Solved On   : 09 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right): return 1
        l, r, sum1 = 1, 1, 0
        if root.left:
            l = self.isSumProperty(root.left)
            sum1 += root.left.data
            if l == 0: return 0
        if root.right:
            r = self.isSumProperty(root.right)
            sum1 += root.right.data
            if r == 0: return 0
        return int(root.data == sum1)

# Time complexity: O(n)
# Space complexity: O(h)