'''
Title     : Max Level Sum in Binary Tree
Domain    : Binary Search Tree, Binary Tree, Tree
Author    : Asmit Singh
Solved On   : 7 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def maxLevelSum(self, root):
        curr = [root]
        ans = root.data
        while curr:
            new = []
            s = 0
            for node in curr:
                s+=node.data
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            ans = max(ans,s)
            curr = new
        return ans
