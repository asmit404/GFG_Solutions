"""
Title     : Distribute candies in a binary tree
Author    : Asmit Singh
Solved On   : 20 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def distributeCandy(self, root):
        def dfs(node):
            if not node: return 0, 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = abs(left[0] - left[1] + right[0] - right[1] + node.data - 1)
            return left[0]+right[0]+node.data, left[1] + right[1] + 1, res + left[2] + right[2]

        left_dfs = dfs(root.left)[2]
        right_dfs = dfs(root.right)[2]
        return left_dfs + right_dfs

# Time Complexity: O(N)
# Space Complexity: O(N)