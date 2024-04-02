'''
Title     : Minimum Absolute Difference In BST
Author    : Asmit Singh
Solved On   : 2 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def absolute_diff(self, root):
        pool = []
        res = float("inf")
        def compute(root):
            if not root: return
            compute(root.left)
            pool.append(root.data)
            compute(root.right)
        compute(root)
        for i in range(1, len(pool)):
            res = min(res, abs(pool[i]-pool[i-1]))
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)