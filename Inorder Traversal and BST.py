"""
Title     : Inorder Traversal and BST
Author    : Asmit Singh
Solved On   : 02 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def isRepresentingBST(self, arr, N):
        return 1 if all(arr[i - 1] <= arr[i] for i in range(1, N)) else 0

# Time Complexity  : O(n)
# Space Complexity : O(1)