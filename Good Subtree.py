'''
Title     : Good Subtrees
Author    : Asmit Singh
Solved On   : 5 May 2023
Solved Using   : Python3
'''

class Solution:
    def goodSubtrees(self, root, k):
        ans = 0
        def solve(root):
            nonlocal ans
            res = set()
            if not root:
                return res
            res.add(root.data)
            res |= solve(root.left)
            res |= solve(root.right)
            if len(res) <= k:
                ans += 1
            return res
        solve(root)
        return ans
