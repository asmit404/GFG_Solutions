"""
Title     : Check if all leaves are at same level
Author    : Asmit Singh
Solved On   : 08 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def check(self, root):
        self.leaf_level = None
        self.same_level = True
        def traverse(node, level):
            if not node: return
            if not node.left and not node.right:
                if self.leaf_level is None:
                    self.leaf_level = level
                elif self.leaf_level != level:
                    self.same_level = False
                return
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        traverse(root, 0)
        return self.same_level

# 250 day streak broken lmao
# Time complexity: O(n)
# Space complexity: O(h)