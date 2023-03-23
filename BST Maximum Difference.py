'''
Title     : BST Maximum Difference
Domain    : DFS, Binary Search Tree, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 23 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def maxDifferenceBST(self, root, target):
        temp = root
        sum = 0
        def solve(root):
            if root == None:
                return 1e9
            if root.left == None and root.right == None:
                return root.data
            left, right = solve(root.left), solve(root.right)
            return root.data + min(left, right)
        while temp:
            if temp.data == target:
                mn = solve(temp)
                return sum - mn + target
            elif temp.data < target:
                sum += temp.data
                temp = temp.right
            else:
                sum += temp.data
                temp = temp.left
        return -1
