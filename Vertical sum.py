'''
Title     : Vertical sum
Author    : Asmit Singh
Solved On   : 5 May 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def verticalSum(self, root):
        dic = {}
        pool = []
        def traverse(root, key):
            if not root: return
            if key not in dic:
                dic[key] = root.data
            else:
                dic[key] += root.data
            traverse(root.left, key-1)
            traverse(root.right, key+1)
        traverse(root, 0)
        for k, v in sorted(dic.items()):
            pool.append(v)
        return pool

# Time Complexity: O(n log n)
# Space Complexity: O(n)