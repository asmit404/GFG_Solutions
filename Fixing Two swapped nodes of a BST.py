'''
Title     : Fixing Two swapped nodes of a BST
Domain    : Binary Search Tree, Data Structures
Author    : Asmit Singh
Solved On   : 19 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def correctBST(self, root):
        def _solve(nd):
            if not nd: return
            nonlocal first, prev
            if _solve(nd.left): return True
            if not first:
                if prev and prev.data > nd.data: 
                    first = prev
            elif first.data < nd.data:
                first.data, prev.data = prev.data, first.data
                return True
            prev = nd
            if _solve(nd.right): return True
            return False
        first, prev = None, None
        if not _solve(root): 
            first.data, prev.data = prev.data, first.data
        return root
