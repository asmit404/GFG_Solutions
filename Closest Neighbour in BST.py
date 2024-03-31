'''
Title     : Closest Neighbour in BST
Author    : Asmit Singh
Solved On   : 31 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def findMaxForN(self, root, n):
        res = -1
        while root:
            if root.key > n:
                root = root.left
            else:
                res = root.key
                root = root.right
        return res

# Time Complexity: O(h)
# Space Complexity: O(1)