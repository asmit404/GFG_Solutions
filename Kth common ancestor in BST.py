'''
Title     : Kth common ancestor in BST
Author    : Asmit Singh
Solved On   : 3 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        if x > y: x, y = y, x
        prev = []
        curr = root

        while curr:
            if curr.data < x:
                prev.append(curr.data)
                curr = curr.right
            elif curr.data > y:
                prev.append(curr.data)
                curr = curr.left
            else:
                prev.append(curr.data)
                if len(prev) < k:
                    return -1
                return prev[-k]
        return -1

# Time Complexity: O(H)
# Space Complexity: O(H)