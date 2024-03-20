'''
Title     : Sum of nodes on the longest path from root to leaf node
Author    : Asmit Singh
Solved On   : 20 Mar 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        def solve(root, h, currsum):
            if root is None: return h, currsum
            l, s1 = solve(root.left, h+1, currsum + root.data)
            r, s2 = solve(root.right, h+1, currsum + root.data)
            if l < r or (l == r and s1 < s2): return r, s2
            return l, s1
        return solve(root, 0, 0)[1]

# Time Complexity: O(n)
# Space Complexity: O(h)