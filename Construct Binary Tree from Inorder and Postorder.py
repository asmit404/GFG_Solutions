'''
Title     : Construct Binary Tree from Inorder and Postorder
Author    : Asmit Singh
Solved On   : 4 May 2024
Solved Using   : Python3
'''

class Solution:
    def buildTree(self, In, post, n):
        if len(In):
            node = Node(post.pop())
            idx = In.index(node.data)
            node.right = self.buildTree(In[idx + 1:], post, n)
            node.left = self.buildTree(In[:idx], post, n)
            return node
        else:
            return None

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)