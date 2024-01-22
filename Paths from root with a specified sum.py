"""
Title     : Paths from root with a specified sum
Author    : Asmit Singh
Solved On   : 22 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def printPaths(self, root, target):
        def dfs(node, path, sum):
            if node:
                path = path + [node.data]
                if sum + node.data == target:
                    res.append(path)
                dfs(node.left, path, sum + node.data)
                dfs(node.right, path, sum + node.data)
        res = []
        dfs(root, [], 0)
        return res

# Time Complexity: O(N)
# Space Complexity: O(N)