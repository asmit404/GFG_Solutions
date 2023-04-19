'''
Title     : Minimum BST Sum Subtree
Domain    : ???
Author    : Asmit Singh
Solved On   : 18 Apr 2023
Solved Using   : Python3
'''

class Solution:
    def minSubtreeSumBST(self, target, root):
        ans = float("inf")

        def func(root):
            nonlocal ans
            if not root:
                return (2, 0, None, None, 0)
            lbst, lsum, lmin, lmax, lsize = func(root.left)
            rbst, rsum, rmin, rmax, rsize = func(root.right)
            if ((lbst == 2) or (lbst == 1 and root.data > lmax)) and ((rbst == 2) or (rbst == 1 and root.data < rmin)):
                s = root.data+lsum+rsum
                size = lsize+rsize+1
                if s == target:
                    ans = min(ans, size)
                return (1, s, lmin if lmin else root.data, rmax if rmax else root.data, size)
            return (0, None, None, None, None)
        func(root)
        return (ans if ans != float("inf") else -1)
