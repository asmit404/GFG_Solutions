'''
Title     : Minimum element in BST
Author    : Asmit Singh
Solved On   : 30 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def minValue(self, root):
        if root is None: return -1
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr.data

# Time Complexity: O(h)
# Space Complexity: O(1)