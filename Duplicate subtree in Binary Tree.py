"""
Title     : Duplicate subtree in Binary Tree
Author    : Asmit Singh
Solved On   : 12 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def dfs(self, root, dic, res):
        if not root:
            return '#'
        left = self.dfs(root.left, dic, res)
        right = self.dfs(root.right, dic, res)
        key = str(root.data) + '|' + left + '|' + right
        if root.left and root.right and key in dic:
            res[0] = True
        dic[key] = True
        return key

    def dupSub(self, root):
        dic = {}
        res = [False]
        self.dfs(root, dic, res)
        return int(res[0])

# Time Complexity: O(N)
# Space Complexity: O(N)